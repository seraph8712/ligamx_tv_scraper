ESPN_CALENDAR_URL = "https://www.espn.com.mx/futbol/calendario/_/liga/mex.1/liga-mx"
ESPN_BROADCAST_URL = "https://www.espn.com.mx/futbol/mexico/nota/_/id/16488137/liga-mx-jornada-13-horarios-y-donde-ver-clausura-2026"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

RAW_CALENDAR_HTML = "data/raw/espn_calendar.html"
RAW_BROADCAST_HTML = "data/raw/espn_broadcast.html"
OUTPUT_JSON = "data/output/ligamx_matches.json"