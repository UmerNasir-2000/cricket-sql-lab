import json
import logging
from pathlib import Path
from typing import Set

logging.basicConfig(level=logging.WARNING)

matches_dir = Path("matches")

unique_teams: Set[str] = set()

for match_file in matches_dir.glob("*.json"):
    with open(match_file, "r", encoding="utf-8") as file:
        match_data = json.load(file)
        match_info = match_data.get("info")

        if match_info is None:
            logging.warning("Missing 'info' section in file: %s", match_file.name)
            continue

        match_teams = match_info.get("teams")

        if match_teams is None:
            logging.warning("Missing 'teams' in file: %s", match_file.name)
            continue

        unique_teams.update(match_teams)

print(len(unique_teams))
