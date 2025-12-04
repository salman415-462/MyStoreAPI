import requests
import json
from config import Config
url=Config.URL
session = requests.Session()
Product_endpoints=Config.PRODUCTS
full_url = f'{url}{Product_endpoints}/21'
res= session.get(full_url)
print(res.json())









class BaseAPI:

    def __init__(self):
        self.url=Config.URL
        self.session = requests.Session()
        self.Product_endpoints=Config.PRODUCTS


    def get(self):
       full_url=f'{self.url}{self.Product_endpoints}'
       g= self.session.get(full_url)
       print(g)