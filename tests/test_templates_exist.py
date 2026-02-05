from pathlib import Path


def test_templates_exist():
    assert Path("templates/report_external.md").exists()
    assert Path("templates/decision_notes.md").exists()
