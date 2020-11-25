from bs4 import BeautifulSoup
import requests
import sqlite3
import sqlalchemy

def call_site(name):
    return requests.get(name).content


soup = BeautifulSoup(call_site("https://www.pccomponentes.com/procesadores"), 'lxml')
products = soup.find("div", id="articleListContent")


def create_list_pccom(array):
    for item in products.find_all("article"):
         array.append({"name": item.attrs["data-name"],"price": item.attrs["data-price"], "img": item.find("img").attrs["src"]})

products_pccom = []
create_list_pccom(products_pccom)

print(str(products_pccom))