import json
from pathlib import Path

from securefim.hasher import calculate_sha256


def create_baseline(directory: str, output_file: str = "baseline.json") -> dict:
    """Create a SHA-256 baseline for all files in a directory."""

    directory_path = Path(directory)

    if not directory_path.is_dir():
        raise NotADirectoryError(f"Directory not found: {directory}")

    baseline = {}

    for file_path in directory_path.rglob("*"):
        if file_path.is_file():
            try:
                relative_path = str(file_path.relative_to(directory_path))
                baseline[relative_path] = calculate_sha256(str(file_path))
            except (PermissionError, OSError) as error:
                print(f"[!] Skipping {file_path}: {error}")

    with Path(output_file).open("w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)

    return baseline