#!/usr/bin/env python3
"""Install skills with preflight conflict checks and transactional rollback."""
from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(folder: Path) -> dict[str, str]:
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are unsupported: {path}')
        if path.is_file():
            result[str(path.relative_to(folder))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def install(root: Path, dest: Path, backup: Path | None = None, dry_run: bool = False) -> dict:
    sources = [root / 'router', *sorted(p.parent for p in (root / 'skills').rglob('SKILL.md'))]
    names = [p.name for p in sources]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate skill names')
    if not sources or not all((p / 'SKILL.md').is_file() for p in sources):
        raise ValueError('Missing SKILL.md')
    dest = dest.expanduser().absolute()
    if dest.is_symlink():
        raise ValueError('Destination must not be a symlink')
    if backup:
        backup = backup.expanduser().absolute()
        if backup.exists():
            raise ValueError('Backup path must be new')
        if backup == dest or dest in backup.parents or backup in dest.parents:
            raise ValueError('Backup must be outside the destination')
    changed, identical, replaced = [], [], []
    for src in sources:
        target = dest / src.name
        src_hash = fingerprint(src)
        if target.is_symlink():
            raise ValueError(f'Destination skill is a symlink: {target}')
        if target.exists():
            if not target.is_dir():
                raise ValueError(f'Destination is not a directory: {target}')
            if fingerprint(target) == src_hash:
                identical.append(src.name)
                continue
            replaced.append(src.name)
        changed.append(src)
    result = {'install': [p.name for p in changed], 'replace': replaced, 'unchanged': identical}
    if dry_run:
        return result
    if replaced and backup is None:
        raise ValueError('Existing skills differ; supply --backup with a new directory. Conflicts: ' + ', '.join(replaced))
    dest.mkdir(parents=True, exist_ok=True)
    # Stage first; no destination skill changes until all copies verify.
    with tempfile.TemporaryDirectory(prefix='.skills-stage-', dir=dest.parent) as stage_dir:
        stage = Path(stage_dir)
        for src in changed:
            shutil.copytree(src, stage / src.name)
            if fingerprint(src) != fingerprint(stage / src.name):
                raise ValueError(f'Staged copy mismatch: {src.name}')
        if backup:
            backup.mkdir(parents=True)
            for name in replaced:
                shutil.copytree(dest / name, backup / name)
        touched = []
        try:
            for src in changed:
                target = dest / src.name
                touched.append(src.name)
                if target.exists():
                    shutil.rmtree(target)
                shutil.move(str(stage / src.name), target)
        except Exception:
            for name in reversed(touched):
                target = dest / name
                if target.exists():
                    shutil.rmtree(target)
                if name in replaced:
                    shutil.copytree(backup / name, target)
            raise
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path.home() / '.codex/skills')
    parser.add_argument('--backup', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        outcome = install(ROOT, args.dest, args.backup, args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Installation failed: {exc}\n')
    print(f"{'Plan' if args.dry_run else 'Installed'}: {len(outcome['install'])}; replaced: {len(outcome['replace'])}; unchanged: {len(outcome['unchanged'])}")
