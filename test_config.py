"""Test that reads from config.json file (file dependency tracking)."""

import json
from pathlib import Path


def test_config_values():
    """Test that config.json has expected values."""
    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config = json.load(f)

    assert config["app_name"] == "TestApp"
    assert config["version"] == "1.0.0"
    assert config["max_retries"] == 3
    assert config["timeout_seconds"] == 30
