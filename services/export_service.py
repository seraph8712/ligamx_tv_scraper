import json
from dataclasses import asdict
from typing import List
from models import Match

def export_json(matches: List[Match], output_path: str) -> None:
    data = [asdict(m) for m in matches]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)