import requests
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_TIME, 'de_DE')

BASE_URL = "http://triathlonranking2.perfectpace.com"
EVENTS_URL = f"{BASE_URL}/events"
RANKING_URL = f"{BASE_URL}/ranking?period=all"


def get_soup(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.Timeout:
        print(f"Request timed out for URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for URL: {url} with error: {e}")
    return None
