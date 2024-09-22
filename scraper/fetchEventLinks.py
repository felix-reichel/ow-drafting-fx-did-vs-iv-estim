import locale
from datetime import datetime

from static import BASE_URL, get_soup, EVENTS_URL

locale.setlocale(locale.LC_TIME, 'de_DE')

START_YEAR = 2024
END_YEAR = 2024


def fetch_event_links():
    events_soup = get_soup(EVENTS_URL)
    events = []

    for article in events_soup.find_all('article', class_='isotopeItem'):
        event_section = article.find('section', class_='boxContent')
        event_link = event_section.find('a')
        event_url = event_link['href']
        event_name = event_link.text.strip()

        event_date_tag = event_section.find('p').text.strip()

        if len(event_date_tag) >= 4:
            try:
                event_year = int(event_date_tag[-4:])

                if START_YEAR <= event_year <= END_YEAR:
                    try:
                        event_date = datetime.strptime(event_date_tag, '%d. %B %Y')
                    except ValueError:
                        event_date = None
                    events.append({
                        'url': f"{BASE_URL}{event_url}",
                        'name': event_name,
                        'date': event_date,
                        'year': event_year,
                        'raw_date': event_date_tag
                    })
            except ValueError:
                print(f"Failed to extract year from date '{event_date_tag}' for event '{event_name}'")
        else:
            print(f"Date string too short for event '{event_name}': '{event_date_tag}'")

        if len(events) > 5:
            break

    return events
