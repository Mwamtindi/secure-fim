import logging
import json
from datetime import datetime
from pathlib import Path


def setup_logger(log_file: str = "logs/securefim.log"):
    """Configure SecureFIM security logging."""

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("SecureFIM")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_path, encoding="utf-8")

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_changes(logger, results: dict):
    """Log detected file integrity changes."""

    for file_path in results["modified"]:
        logger.warning(f"FILE_MODIFIED | {file_path}")

    for file_path in results["new"]:
        logger.warning(f"FILE_CREATED | {file_path}")

    for file_path in results["deleted"]:
        logger.warning(f"FILE_DELETED | {file_path}")


def generate_report(
    results: dict,
    directory: str,
    output_file: str = "report.json"
) -> dict:
    """Generate a JSON report of detected file integrity changes."""

    report = {
        "scan_time": datetime.now().isoformat(timespec="seconds"),
        "directory": directory,
        "summary": {
            "modified": len(results["modified"]),
            "new": len(results["new"]),
            "deleted": len(results["deleted"]),
        },
        "changes": {
            "modified": results["modified"],
            "new": results["new"],
            "deleted": results["deleted"],
        },
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return report