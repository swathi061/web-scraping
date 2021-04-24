import requests
from bs4 import BeautifulSoup
import pandas as pd 
  
URL = "https://store.hp.com/in-en/default/laptops-tablets.html?hp_facet_processortype=Intel+Core+i5"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
products = []
prices = []
table = soup.find('div', attrs = {'class':'category-tabs product data items'}) 
for row in table.findAll('div',attrs = {'class':'product-item-info'}):
    price=row.find('span', attrs={'class':'price'})
    name=row.find('a', attrs={'class':'product-item-link'})
    products.append(name.text.strip())
    prices.append(price.text.strip())
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
