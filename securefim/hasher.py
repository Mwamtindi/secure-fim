import hashlib
from pathlib import Path


def calculate_sha256(file_path: str) -> str:
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    try:
        with Path(file_path).open("rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")