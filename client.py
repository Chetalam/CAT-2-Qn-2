import requests

BASE_URL = 'http://127.0.0.1:8000/products/'

def add_product(name, description, price):
    response = requests.post(BASE_URL, json={
        'name': name,
        'description': description,
        'price': price
    })
    if response.status_code == 201:
        print(f'Product created with ID: {response.json()["id"]}')
    else:
        print(f'Failed to create product: {response.json()}')

def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(product)
    else:
        print('Failed to retrieve products')

if __name__ == '__main__':
    # Example usage
    add_product('Sample Product', 'This is a sample product.', 19.99)
    get_products()