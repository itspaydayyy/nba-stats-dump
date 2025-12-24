import json
from datetime import datetime
from nba_api.stats.endpoints import leaguedashteamstats

SEASON = "2024-25"
SEASON_TYPE = "Regular Season"
PER_MODE = "PerGame"

def fetch(last_n_games: int):
    r = leaguedashteamstats.LeagueDashTeamStats(
        measure_type_detailed_defense="Advanced",
        per_mode_detailed=PER_MODE,
        season=SEASON,
        season_type_all_star=SEASON_TYPE,
        last_n_games=last_n_games,
        timeout=45
    )
    return r.get_dict()

def main():
    payload = {
        "meta": {
            "season": SEASON,
            "seasonType": SEASON_TYPE,
            "perMode": PER_MODE,
            "generatedAtUTC": datetime.utcnow().isoformat() + "Z"
        },
        "season": fetch(0),
        "last10": fetch(10),
        "last5": fetch(5)
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(payload, f)

if __name__ == "__main__":
    main()
