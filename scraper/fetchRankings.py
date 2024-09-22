import pandas as pd

from static import BASE_URL, get_soup


def fetch_rankings(rank_type=1):
    rankings = []
    page = 1

    while True:
        url = f"{BASE_URL}/ranking?period=all&type={rank_type}&page={page}"
        soup = get_soup(url)

        table = soup.find('table', {'class': 'table-striped'})
        if not table:
            break

        for row in table.find('tbody').find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 5:
                rankings.append({
                    'rank': cols[0].text.strip(),
                    'last_name': cols[1].text.strip(),
                    'first_name': cols[2].text.strip(),
                    'events': cols[3].text.strip(),
                    'percent_behind': cols[4].text.strip(),
                    'athlete_url': BASE_URL + cols[1].find('a')['href']
                })

        next_page = soup.find('li', {'class': 'next'})
        if not next_page:
            break
        page += 1

    return rankings


if __name__ == "__main__":
    rankings = fetch_rankings(rank_type=1)
    df_rankings = pd.DataFrame(rankings)
    df_rankings.to_csv('rankings_type1.csv', index=False)
    print(df_rankings.head())
