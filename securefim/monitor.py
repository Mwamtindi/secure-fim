import time
from pathlib import Path

from securefim.hasher import calculate_sha256
from securefim.reporter import setup_logger, log_changes


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

    for file_path, current_hash in current_files.items():
        if file_path not in baseline:
            new_files.append(file_path)
        elif baseline[file_path] != current_hash:
            modified.append(file_path)

    for file_path in baseline:
        if file_path not in current_files:
            deleted.append(file_path)

    return {
        "modified": modified,
        "new": new_files,
        "deleted": deleted,
    }


def monitor_directory(
    directory: str,
    baseline: dict,
    interval: int = 10,
):
    """Continuously monitor a directory for integrity changes."""

    logger = setup_logger()

    print(f"[+] Monitoring: {directory}")
    print(f"[+] Scan interval: {interval} seconds")
    print("[+] Press Ctrl+C to stop.\n")

    try:
        while True:
            results = scan_directory(directory, baseline)

            has_changes = any(results.values())

            if has_changes:
                print("\n[!] File integrity changes detected!")

                for file_path in results["modified"]:
                    print(f"[MODIFIED] {file_path}")

                for file_path in results["new"]:
                    print(f"[NEW] {file_path}")

                for file_path in results["deleted"]:
                    print(f"[DELETED] {file_path}")

                # Log detected security events.
                log_changes(logger, results)

                # Update the in-memory baseline so the same
                # event is not reported repeatedly.
                for file_path in results["modified"]:
                    baseline[file_path] = calculate_sha256(
                        str(Path(directory) / file_path)
                    )

                for file_path in results["new"]:
                    baseline[file_path] = calculate_sha256(
                        str(Path(directory) / file_path)
                    )

                for file_path in results["deleted"]:
                    baseline.pop(file_path, None)

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped.")