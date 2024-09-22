import pandas as pd

from static import BASE_URL, get_soup


def fetch_athlete_details(athlete_id):
    athlete_results = []
    url = f"{BASE_URL}/athlete/{athlete_id}"
    soup = get_soup(url)

    table = soup.find('table', {'class': 'table-striped'})
    if not table:
        return []

    for row in table.find('tbody').find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 6:
            athlete_results.append({
                'event_date': cols[0].text.strip().split('<br />')[0].strip(),
                'event_name': cols[0].find('a').text.strip(),
                'swim_percent_diff': cols[1].find('td', text="Diff:").find_next_sibling().text.strip(),
                'bike_percent_diff': cols[2].find('td', text="Diff:").find_next_sibling().text.strip(),
                'run_percent_diff': cols[3].find('td', text="Diff:").find_next_sibling().text.strip(),
                'overall_percent_diff': cols[4].find('td', text="Diff:").find_next_sibling().text.strip(),
                'event_type': cols[5].find('span').text.strip() if cols[5].find('span') else ''
            })

    return athlete_results
