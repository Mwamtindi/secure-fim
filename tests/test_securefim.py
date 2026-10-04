import json

from securefim.hasher import calculate_sha256
from securefim.baseline import create_baseline
from securefim.monitor import scan_directory


def test_sha256_hash(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello")

    first_hash = calculate_sha256(str(file_path))
    second_hash = calculate_sha256(str(file_path))

    assert first_hash == second_hash
    assert len(first_hash) == 64


def test_create_baseline(tmp_path):
    file_path = tmp_path / "important.txt"
    file_path.write_text("original")

    baseline_file = tmp_path / "baseline.json"

    baseline = create_baseline(
        str(tmp_path),
        str(baseline_file)
    )

    assert "important.txt" in baseline
    assert baseline_file.exists()

    with baseline_file.open("r", encoding="utf-8") as file:
        saved_baseline = json.load(file)

    assert saved_baseline == baseline


def test_detect_modified_file(tmp_path):
    file_path = tmp_path / "important.txt"
    file_path.write_text("original")

    baseline = create_baseline(str(tmp_path))

    file_path.write_text("modified")

    results = scan_directory(str(tmp_path), baseline)

    assert "important.txt" in results["modified"]


def test_detect_new_file(tmp_path):
    original_file = tmp_path / "important.txt"
    original_file.write_text("original")

    baseline = create_baseline(str(tmp_path))

    new_file = tmp_path / "suspicious.txt"
    new_file.write_text("suspicious")

    results = scan_directory(str(tmp_path), baseline)

    assert "suspicious.txt" in results["new"]


def test_detect_deleted_file(tmp_path):
    file_path = tmp_path / "important.txt"
    file_path.write_text("original")

    baseline = create_baseline(str(tmp_path))

    file_path.unlink()

    results = scan_directory(str(tmp_path), baseline)

    assert "important.txt" in results["deleted"]