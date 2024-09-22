import pandas as pd

from static import get_soup, BASE_URL


def fetch_event_results(event_url):
    results = []
    page = 1

    while True:
        soup = get_soup(event_url + '?Result_page=' + str(page))

        if soup is None:
            print(f"Failed to retrieve page {page} for event {event_url}")
            break

        table = soup.find('table', {'class': 'table-striped'})
        if not table:
            print(f"No results found for event {event_url} on page {page}")
            break

        for row in table.find('tbody').find_all('tr'):
            cols = row.find_all('td')
            print('result for no.:' + cols[0].text.strip())
            if len(cols) >= 8:
                results.append({
                    'event_url': event_url,
                    'rank': cols[0].text.strip(),
                    'last_name': cols[1].text.strip(),
                    'first_name': cols[2].text.strip(),
                    'nationality': cols[3].text.strip(),
                    'total_time': cols[4].text.strip(),
                    'swim_time': cols[5].text.strip(),
                    'bike_time': cols[6].text.strip(),
                    'run_time': cols[7].text.strip(),
                    'athlete_url': BASE_URL + cols[1].find('a')['href']
                })

        next_page = soup.find('li', {'class': 'next'})
        if not next_page:
            break

        # Temporary
        if page > 5:
            break
        page += 1

    return results


if __name__ == "__main__":
    event_results = fetch_event_results(1754)
    df_event_results = pd.DataFrame(event_results)
    df_event_results.to_csv('event_results_1754.csv', index=False)