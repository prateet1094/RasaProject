import requests
import json
import re
from types import SimpleNamespace


def fetchProducts(searchTerm):
    response = requests.get('https://api.dominos.co.in/prod-olo-api/v1/65937/menu/data')
    menuObj = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
    matchingProducts = []
    for categories in menuObj.data:
        for products in categories.data:
            if re.search(searchTerm, products.name, re.IGNORECASE):
                matchingProducts.append(products)

    

 
    # returning sum of a and b
    return matchingProducts;