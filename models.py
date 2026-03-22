from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Match:
    competition: str
    date_text: str
    home_team: str
    away_team: str
    kickoff_time_cdmx: str
    venue: Optional[str] = None  #indica que puede ser una cadena de texto o no
    city: Optional[str] = None
    country: Optional[str] = None
    broadcast_mx: List[str] = field(default_factory=list)
    source_calendar: Optional[str] = None
    source_broadcast: Optional[str] = None