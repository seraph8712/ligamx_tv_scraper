import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

from config import ESPN_BROADCAST_URL, DEFAULT_HEADERS, RAW_BROADCAST_HTML
from utils import clean_text, normalize_team_name, normalize_broadcast_list

def fetch_broadcast_html() -> str:
    response = requests.get(ESPN_BROADCAST_URL, headers=DEFAULT_HEADERS, timeout=20)
    response.raise_for_status()
    html = response.text

    with open(RAW_BROADCAST_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    return html

def parse_broadcast_html(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text("\n")

    pattern = re.compile(
        r"(.*?)\s*Fecha:\s*(.*?)\s*Horario:\s*(.*?)\s*Lugar:\s*(.*?)\s*¿Dónde ver\?:\s*(.*?)(?=\n\s*[A-ZÁÉÍÓÚÑ].*?\s+vs\s+.*?\n|$)",
        re.DOTALL
    )

    results = []

    for match in pattern.finditer(text):
        title = clean_text(match.group(1))
        fecha = clean_text(match.group(2))
        horario = clean_text(match.group(3))
        lugar = clean_text(match.group(4))
        donde_ver = clean_text(match.group(5))

        if " vs " not in title:
            continue

        home, away = [normalize_team_name(x) for x in title.split(" vs ", 1)]

        results.append({
            "home_team": home,
            "away_team": away,
            "date_text": fecha,
            "kickoff_time_cdmx": horario,
            "venue": lugar,
            "broadcast_mx": normalize_broadcast_list(donde_ver),
            "source_broadcast": ESPN_BROADCAST_URL,
        })

    return results

def scrape_broadcast() -> List[dict]:
    html = fetch_broadcast_html()
    return parse_broadcast_html(html)