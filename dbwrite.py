import sqlite3

conn = sqlite3.connect(r"C:\Users\zeus\OneDrive\Documents\pcpartpicker_alternative\products.db")

c = conn.cursor()


def _writeToDb_(table, data):
    c = conn.cursor()

    c.execute("""INSERT INTO products(name, price, image) 
            VALUES (?,?,?);""", (data.cpu, data.price, data.image))

    conn.commit()

    conn.close()