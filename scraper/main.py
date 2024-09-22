import pandas as pd

from fetchAthleteDetails import fetch_athlete_details
from fetchEventLinks import fetch_event_links
from fetchEventResults import fetch_event_results
from fetchRankings import fetch_rankings


def main():
    events = fetch_event_links()

    all_results = []

    athlete_details = []

    for event in events:
        print(f"Fetching results for event: {event['name']} on {event['date']}")

        results = fetch_event_results(event['url'])
        all_results.extend(results)

        for result in results:
            """
            print(f"Fetching athlete details for {result['first_name']} {result['last_name']}")
    
            athlete_data = fetch_athlete_details(result['athlete_url'])
            athlete_details.append({
                'athlete': f"{result['first_name']} {result['last_name']}",
                'details': athlete_data
            })
            """

    pd.DataFrame(events).to_csv('events_2016_2024.csv', index=False)
    pd.DataFrame(all_results).to_csv('event_results.csv', index=False)

    # sprint_rankings = fetch_rankings(rank_type=1)
    # mittel_rankings = fetch_rankings(rank_type=2)

    # pd.DataFrame(sprint_rankings).to_csv('sprint_rankings.csv', index=False)
    # pd.DataFrame(mittel_rankings).to_csv('mittel_rankings.csv', index=False)

    # pd.DataFrame(athlete_details).to_csv('athlete_details.csv', index=False)


if __name__ == "__main__":
    main()
