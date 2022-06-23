from json import dumps, loads
from auth_service import get_current_user

PRODUCTS_DB_FILE_PATH = './db/products.txt'


def get_all_products():
    with open(PRODUCTS_DB_FILE_PATH, 'r') as products_file:
        return [loads(line.strip()) for line in products_file]

def buy_product(product_id):
    user=get_current_user()
