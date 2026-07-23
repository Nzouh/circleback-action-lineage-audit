# Circleback action lineage audit

A compact review gate for meeting-derived actions. It checks transcript lineage, ownership, date consistency, and whether low-confidence actions are set to auto-dispatch.

```bash
python audit.py example.json -o report.json
python -m unittest -v
```

The synthetic sample intentionally exits `2`. This does not transcribe meetings or compete with a notetaker; it validates the handoff from an extracted action to a downstream workflow.
