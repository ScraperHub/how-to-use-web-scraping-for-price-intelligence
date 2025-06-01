from amazon_serp_scraper import get_products_from_amazon
from ebay_serp_scraper import get_products_from_ebay

def get_structured_consolidated_data(query: str, country: str = None, top_level_domain: str = 'com') -> list[dict]:
    products = []

    amazon_data = get_products_from_amazon(query, country=country, top_level_domain=top_level_domain)
    products.extend([{"name": item['name'], "price": item['price'], "url": item['url'], "source": "Amazon"} for item in amazon_data])

    ebay_data = get_products_from_ebay(query, country=country, top_level_domain=top_level_domain)
    products.extend([{"name": item['title'], "price": item['price']['current']['to'].strip(), "url": item['url'], "source": "Ebay"} for item in ebay_data])

    return products


if __name__ == "__main__":

    import json

    products = get_structured_consolidated_data("Apple iPhone 15 Pro Max 256GB", country="US", top_level_domain="co.uk")

    pretty_json = json.dumps(products, indent=2)
    print(pretty_json)
