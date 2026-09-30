from pathlib import Path

from securefim.hasher import calculate_sha256


def scan_directory(directory: str, baseline: dict) -> dict:
    """Compare the current directory state against the saved baseline."""

    directory_path = Path(directory)

    if not directory_path.is_dir():
        raise NotADirectoryError(f"Directory not found: {directory}")

    current_files = {}

    for file_path in directory_path.rglob("*"):
        if file_path.is_file():
            try:
                relative_path = str(file_path.relative_to(directory_path))
                current_files[relative_path] = calculate_sha256(str(file_path))
            except (PermissionError, OSError) as error:
                print(f"[!] Skipping {file_path}: {error}")

    modified = []
    new_files = []
    deleted = []

    # Detect new and modified files
    for file_path, current_hash in current_files.items():
        if file_path not in baseline:
            new_files.append(file_path)
        elif baseline[file_path] != current_hash:
            modified.append(file_path)

    # Detect deleted files
    for file_path in baseline:
        if file_path not in current_files:
            deleted.append(file_path)

    return {
        "modified": modified,
        "new": new_files,
        "deleted": deleted,
    }