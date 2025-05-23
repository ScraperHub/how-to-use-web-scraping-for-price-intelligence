import requests
import urllib.parse
from requests.exceptions import RequestException

def get_products_from_ebay(query: str, country: str = None, top_level_domain: str = 'com') -> list[dict]:
    API_TOKEN = "<Normal requests token>"
    API_ENDPOINT = "https://api.crawlbase.com/"

    params = {
        "token": API_TOKEN,
        "url": f"https://www.ebay.{top_level_domain}/sch/i.html?_nkw={urllib.parse.quote_plus(query)}",
        "scraper": "ebay-serp",
        "country": country
    }

    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    result = response.json()

    return result['body']['products']

if __name__ == "__main__":

    print(get_products_from_ebay("Apple iPhone 15 Pro Max 256GB", country="US", top_level_domain="co.uk"))
