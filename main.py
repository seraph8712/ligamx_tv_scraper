from scrappers.espn_calendar import scrape_calendar
from scrappers.espn_broadcast import scrape_broadcast
from services.merge_service import merge_matches
from services.export_service import export_json
from config import OUTPUT_JSON

def main():
    calendar_matches = scrape_calendar()
    broadcast_items = scrape_broadcast()

    final_matches = merge_matches(calendar_matches, broadcast_items)

    print(f"Partidos encontrados: {len(final_matches)}")
    for m in final_matches:
        print(
            f"{m.date_text} | "
            f"{m.home_team} vs {m.away_team} | "
            f"{m.kickoff_time_cdmx} | "
            f"{m.venue} | "
            f"{', '.join(m.broadcast_mx) if m.broadcast_mx else 'Sin transmisión detectada'}"
        )

    export_json(final_matches, OUTPUT_JSON)
    print(f"Archivo generado: {OUTPUT_JSON}")

if __name__ == "__main__":
    main()