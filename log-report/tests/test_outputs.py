import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.is_file(), "missing /app/report.json"
    try:
        return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc


def test_report_schema():
    """Success criterion 1: the artifact is a JSON object with exactly the required keys."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty log entries."""
    report = load_report()
    assert type(report.get("total_requests")) is int
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct first-field IPs."""
    report = load_report()
    assert type(report.get("unique_ips")) is int
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequent quoted HTTP request path."""
    report = load_report()
    assert isinstance(report.get("top_path"), str)
    assert report["top_path"] == "/index.html"
