import requests
import urllib.parse
from requests.exceptions import RequestException

def get_products_from_amazon(query: str, country: str = None, top_level_domain: str = 'com') -> list[dict]:
    API_TOKEN = "<Normal requests token>"
    API_ENDPOINT = "https://api.crawlbase.com/"

    params = {
        "token": API_TOKEN,
        "url": f"https://www.amazon.{top_level_domain}/s?k={urllib.parse.quote_plus(query)}",
        "scraper": "amazon-serp",
        "country": country
    }

    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    result = response.json()

    return result['body']['products']

if __name__ == "__main__":

    import json

    products = get_products_from_amazon("Apple iPhone 15 Pro Max 256GB", country="US", top_level_domain="co.uk")
    pretty_json = json.dumps(products, indent=2)
    print(pretty_json)
