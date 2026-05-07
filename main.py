import json
from pathlib import Path

matches_dir = Path("matches")

for file_path in matches_dir.glob("*.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
