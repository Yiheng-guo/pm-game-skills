# Development

Use Python 3.10+ (3.12 recommended). No third-party dependency is required for the validator or installer. The inherited asset tooling uses Pillow.

```bash
python3 scripts/validate-skills.py
python3 -m unittest discover -s tests -v
python3 scripts/generate-site.py
python3 scripts/check-site.py
```

Each changed engine/discipline/genre skill has three observable acceptance scenarios. Run them in the target runtime when working on that feature. Structural validation cannot prove the gameplay outcomes. Keep the upstream reference and verify the actual project version before changing version-sensitive snippets.

The catalog is `docs/skill-catalog.json`. Add a new skill to the router table and matching marketplace bundles. New product workflows are composed for whole-game work; do not force a full product process onto a one-line fix.
