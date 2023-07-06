import openai
import requests
import base64

# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Set Woocommerce store URL
store_url = "https://yourstore.com"

# Set Woocommerce API keys
woocommerce_key = "WOOCOMMERCE_API_KEY"
woocommerce_secret = "WOOCOMMERCE_API_SECRET"

# Base64 encoding of the Woocommerce API keys
token = base64.b64encode(f"{woocommerce_key}:{woocommerce_secret}".encode()).decode("ascii")

def generate_description(product_name, product_features, product_category):
    # Define and generate product description using GPT-3

    prompt = f"Generate a description for a {product_category} product named '{product_name}' with the following features: {product_features}"

    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
    )

    # Extract the generated description
    return response.choices[0].text.strip()

def get_products(page):
    # Fetch products from Woocommerce store using API

    endpoint = f"{store_url}/wp-json/wc/v3/products"
    headers = {
        "Authorization": f"Basic {token}"
    }
    params = {
        "per_page": 100,  # Limit of items per request
        "page": page  # Page number to get
    }
    response = requests.get(endpoint, headers=headers, params=params)
    return response.json()

def update_product(product_id, description):
    # Update product description in Woocommerce

    endpoint = f"{store_url}/wp-json/wc/v3/products/{product_id}"
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }
    data = {
        "description": description
    }
    response = requests.put(endpoint, headers=headers, json=data)
    return response.status_code

# Initiate pagination at page 1
page = 1

# Start looping through all products
while True:
    # Get a page of products
    products = get_products(page)

    # If no products returned, end the loop
    if not products:
        break

    # Loop through each product
    for product in products:
        product_name = product["name"]
        product_category = product["categories"][0]["name"]
        product_features = ",".join([feature["name"] for feature in product["attributes"]])
        
        # Generate the product description using GPT-3
        generated_description = generate_description(product_name, product_features, product_category)
        
        # Update the product with the generated description
        product_id = product["id"]
        update_status = update_product(product_id, generated_description)
        
        # Check the update status
        if update_status == 200:
            print(f"Product '{product_name}' updated with the generated description")
        else:
            print(f"Failed to update product '{product_name}'")

    # Move on to the next page
    page += 1
