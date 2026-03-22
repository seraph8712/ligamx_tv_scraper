from typing import List
from models import Match

def merge_matches(calendar_matches: List[Match], broadcast_items: List[dict]) -> List[Match]:
    index = {}

    for item in broadcast_items:
        key = (
            item["home_team"].lower(),
            item["away_team"].lower(),
        )
        index[key] = item

    merged = []

    for match in calendar_matches:
        key = (match.home_team.lower(), match.away_team.lower())
        extra = index.get(key)

        if extra:
            match.broadcast_mx = extra.get("broadcast_mx", [])
            match.source_broadcast = extra.get("source_broadcast")
            if not match.venue and extra.get("venue"):
                match.venue = extra["venue"]

        merged.append(match)

    return merged