import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('installer', Path(__file__).parents[1] / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / 'repo'
        for name in ['router', 'skills/workflows/example']:
            folder = self.root / name
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text('new')
            (folder / 'references').mkdir()
            (folder / 'references/case.md').write_text('scenario')
        self.dest = self.base / 'installed'

    def test_copy_resources_and_idempotence(self):
        self.assertEqual(len(installer.install(self.root, self.dest)['install']), 2)
        self.assertEqual((self.dest / 'example/references/case.md').read_text(), 'scenario')
        self.assertEqual(len(installer.install(self.root, self.dest)['unchanged']), 2)

    def test_conflict_preflight_preserves_all_skills(self):
        (self.dest / 'example').mkdir(parents=True)
        (self.dest / 'example/SKILL.md').write_text('old')
        with self.assertRaises(ValueError):
            installer.install(self.root, self.dest)
        self.assertFalse((self.dest / 'router').exists())
        self.assertEqual((self.dest / 'example/SKILL.md').read_text(), 'old')

    def test_backup_and_rollback_after_failed_move(self):
        installer.install(self.root, self.dest)
        (self.dest / 'example/SKILL.md').write_text('old')
        (self.dest / 'router/SKILL.md').write_text('old-router')
        original = installer.shutil.move
        calls = []
        def fail_second(src, dst):
            calls.append(dst)
            if len(calls) == 2:
                raise OSError('simulated disk failure')
            return original(src, dst)
        with patch.object(installer.shutil, 'move', side_effect=fail_second):
            with self.assertRaises(OSError):
                installer.install(self.root, self.dest, self.base / 'backup')
        self.assertEqual((self.dest / 'router/SKILL.md').read_text(), 'old-router')
        self.assertEqual((self.dest / 'example/SKILL.md').read_text(), 'old')

    def test_dry_run_is_read_only(self):
        installer.install(self.root, self.dest, dry_run=True)
        self.assertFalse(self.dest.exists())

    def test_nested_backup_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.root, self.dest, self.dest / 'backup')

    def test_symlink_rejected(self):
        (self.root / 'router/references/link').symlink_to('/tmp')
        with self.assertRaises(ValueError):
            installer.install(self.root, self.dest)
