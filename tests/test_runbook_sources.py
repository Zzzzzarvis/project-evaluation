from pathlib import Path


def test_runbook_mentions_sources():
    text = Path("docs/runbook.md").read_text()
    assert "Nansen" in text and "Dune" in text
