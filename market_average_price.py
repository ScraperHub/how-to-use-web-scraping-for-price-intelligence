import pandas as pd
from price_parser import Price
from structured_consolidated_data import get_structured_consolidated_data

products = get_structured_consolidated_data("Apple iPhone 15 Pro Max 256GB", country="US", top_level_domain="co.uk")
products_with_prices = filter(lambda product: (product["price"] is not None and product["price"].strip() != ''), products)
sanitized_products = [product | {"price": float(Price.fromstring(product["price"]).amount) } for product in products_with_prices]

data = list(sanitized_products)
df = pd.DataFrame(data)

# Check data types and examine the source column
iphone_mask = df['product'].str.contains('iPhone', case=False, na=False)

# Calculate average prices for iPhone models by source
iphone_df = df[df['product'].str.contains('iPhone', case=False, na=False)]

# Group by source and calculate average prices
avg_prices = iphone_df.groupby('source')['price'].agg(['mean', 'count']).round(2)
avg_prices.columns = ['Average Price (£)', 'Number of Products']

print("\n\nAverage iPhone prices by source:")
print(avg_prices)

# Calculate the difference
amazon_avg = avg_prices.loc['Amazon', 'Average Price (£)']
ebay_avg = avg_prices.loc['Ebay', 'Average Price (£)']
difference = amazon_avg - ebay_avg

print("\n\nPrice comparison:")
print(f"Amazon average: £{amazon_avg}")
print(f"eBay average: £{ebay_avg}")
print(f"Difference: £{difference:.2f} (Amazon is {'higher' if difference > 0 else 'lower'} than eBay)\n\n")
