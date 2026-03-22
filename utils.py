def clean_text(value: str) -> str:
    return " ".join(value.split()).strip()

def normalize_team_name(name: str) -> str:
    aliases = {
        "guadalajara": "Chivas",
        "pumas unam": "Pumas",
        "mazatlán fc": "Mazatlán",
    }
    key = clean_text(name).lower()
    return aliases.get(key, clean_text(name))

def split_location(text: str):
    parts = [p.strip() for p in text.split(",")]
    venue = parts[0] if len(parts) > 0 else None
    city = parts[1] if len(parts) > 1 else None
    country = parts[2] if len(parts) > 2 else None
    return venue, city, country

def normalize_broadcast_list(text: str):
    if not text:
        return []
    text = text.replace(" y ", ", ")
    return [item.strip() for item in text.split(",") if item.strip()]