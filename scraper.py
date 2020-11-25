from bs4 import BeautifulSoup
import requests
import sqlite3


class product():
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image


pccomponentes = requests.get("https://www.pccomponentes.com/procesadores/amd")



soup = BeautifulSoup(pccomponentes.content, 'lxml')
products = soup.find("div", id="articleListContent")



for item in products.find_all("a"):
    print(item.get_text())




for item in products.find_all("a"):
    cpu.append(item.get_text().replace(" ","-"))
    

for item in products.find_all("span"):
    if item.get_text()[-1::] == "€":
        price.append(item.get_text().replace(" ","-"))

for image in products.find_all("img"):
    images.append(str(image["src"]))

conn = sqlite3.connect(r"C:\Users\zeus\OneDrive\Documents\pcpartpicker_alternative\products.db")

c = conn.cursor()

# Create table

# Insert a row of data

for item in range(len(images)):
    c.execute("""INSERT INTO products(name, price, image) 
               VALUES (?,?,?);""", (cpu[item], price[item], images[item]))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

