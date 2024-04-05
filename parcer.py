import requests
from bs4 import BeautifulSoup
import json

products_id = []
products_response = requests.get("https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html")
soup = BeautifulSoup(products_response.text, 'html.parser')  # parse every product id

for product in soup.find_all('li', class_='cmp-category__item'):
    if product['data-product-id'] != '7629':  # not exists in Ukraine
        products_id.append(product['data-product-id'])

result = {}
for product_id in products_id:
    url = 'https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item='
    url = url + str(product_id)
    response = requests.get(url).json()

    name = response['item']['item_name']  # name
    subresult = {}
    description = response['item']['description']  # description
    subresult['Загальна інформація'] = description
    for el in response['item']['nutrient_facts']['nutrient']:
        subresult[el['name']] = el['value']
    result[name] = subresult

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
