from pathlib import Path


def test_skill_files_exist():
    required = [
        "skills/dex_project_evaluator/SKILL.md",
        "skills/dex_coordinator/SKILL.md",
        "skills/dex_contract_security/SKILL.md",
        "skills/dex_liquidity_tokenomics/SKILL.md",
        "skills/dex_market_compliance/SKILL.md",
        "skills/dex_community_growth/SKILL.md",
        "skills/dex_team_background/SKILL.md",
        "skills/dex_product_tech/SKILL.md",
        "skills/dex_onchain_fundsflow/SKILL.md",
        "skills/dex_internal_decision/SKILL.md",
    ]
    for path in required:
        assert Path(path).exists(), path
