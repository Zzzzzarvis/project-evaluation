from pathlib import Path
from scripts.telegram_notify import send_message


def extract_summary(report_path: Path, decision_path: Path) -> str:
    report_text = Path(report_path).read_text(encoding="utf-8")
    decision_text = Path(decision_path).read_text(encoding="utf-8")

    report_lines = [line for line in report_text.splitlines() if line.strip()]
    summary_lines = report_lines[:8]

    decision_lines = []
    for line in decision_text.splitlines():
        if "建议结果" in line or "置信度" in line:
            decision_lines.append(line.strip())

    parts = ["[评估完成]", *summary_lines]
    if decision_lines:
        parts.append("\n内部结论：")
        parts.extend(decision_lines)

    return "\n".join(parts)


def main() -> None:
    report_path = Path("report.md")
    decision_path = Path("decision_notes.md")
    text = extract_summary(report_path, decision_path)
    send_message(text)


if __name__ == "__main__":
    main()
