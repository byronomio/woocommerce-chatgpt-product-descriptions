# WooCommerce Product Description Generator

 A Python script that automatically generates product descriptions using OpenAI's GPT-3 and updates the descriptions for each product on a WooCommerce store.

## Prerequisites

- Python 3.x
- WooCommerce store with products
- OpenAI API key
- WooCommerce API keys

## Setup and Installation

1. Clone the repository to your local machine.
2. Install required Python packages:

    ```
    pip install openai requests
    ```

3. Replace `YOUR_OPENAI_API_KEY`, `https://yourstore.com`, `WOOCOMMERCE_API_KEY`, and `WOOCOMMERCE_API_SECRET` with your actual OpenAI API key, WooCommerce store URL, and WooCommerce API keys respectively in the script.


The script fetches products from the WooCommerce store, generates descriptions using GPT-3, and updates the products with these descriptions.

## Functions

The script contains the following main functions:

- `generate_description(product_name, product_features, product_category)`: This function takes in a product name, product features, and product category as arguments, uses OpenAI's GPT-3 to generate a product description, and returns the description.

- `get_products(page)`: This function retrieves a page of products from the WooCommerce store via the `/wp-json/wc/v3/products` endpoint. It uses pagination to fetch all products, fetching 100 products per page.

- `update_product(product_id, description)`: This function updates a product's description on the WooCommerce store. It takes a product ID and the generated description as arguments, and returns the status code of the API request.

The script loops through all products, generating and updating descriptions for each product. The loop continues to fetch new pages of products until no products are left.

## Notes

Make sure you have the necessary API keys and correct permissions to fetch and update products on your WooCommerce store. The number of products per page is set to 100, but you can adjust this number as needed.

This script doesn't handle errors in depth, so you might want to add more sophisticated error handling depending on your needs.
