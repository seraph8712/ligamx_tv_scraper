import requests
from bs4 import BeautifulSoup
from typing import List

from config import ESPN_CALENDAR_URL, DEFAULT_HEADERS, RAW_CALENDAR_HTML
from models import Match
from utils import clean_text, split_location, normalize_team_name

def fetch_calendar_html() -> str:
    response = requests.get(ESPN_CALENDAR_URL, headers=DEFAULT_HEADERS, timeout=20)
    response.raise_for_status()
    html = response.text

    with open(RAW_CALENDAR_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    return html

def parse_calendar_html(html: str) -> List[Match]:
    soup = BeautifulSoup(html, "lxml")
    lines = [clean_text(x) for x in soup.get_text("\n").splitlines()]
    lines = [x for x in lines if x]

    matches = []
    current_date = None
    i = 0

    while i < len(lines):
        line = lines[i]

        if "," in line and "2026" in line:
            current_date = line
            i += 1
            continue

        if i + 4 < len(lines):
            home = lines[i]
            versus = lines[i + 1]
            away = lines[i + 2]
            kickoff = lines[i + 3]
            location = lines[i + 4]

            looks_like_match = (
                versus.lower() == "v"
                and ("AM" in kickoff or "PM" in kickoff)
                and current_date is not None
                and ("," in location or "Estadio" in location)
            )

            if looks_like_match:
                venue, city, country = split_location(location)
                matches.append(
                    Match(
                        competition="Liga MX",
                        date_text=current_date,
                        home_team=normalize_team_name(home),
                        away_team=normalize_team_name(away),
                        kickoff_time_cdmx=kickoff,
                        venue=venue,
                        city=city,
                        country=country,
                        source_calendar=ESPN_CALENDAR_URL,
                    )
                )
                i += 5
                continue

        i += 1

    return matches

def scrape_calendar() -> List[Match]:
    html = fetch_calendar_html()
    return parse_calendar_html(html)