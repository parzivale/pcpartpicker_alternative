from bs4 import BeautifulSoup
import requests
import sqlite3


def call_site(name):
    return requests.get(name).content


soup = BeautifulSoup(call_site("https://www.pccomponentes.com/procesadores/amd"), 'lxml')
products = soup.find("div", id="articleListContent")



for item in products.find_all("article"):
    print(item.attrs["data-name"],item.attrs["data-price"],item.find("img").attrs["src"])