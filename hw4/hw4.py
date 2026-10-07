import csv


def save_books(books):
    with open('books.txt', 'w', encoding='utf-8') as file:
        for book in books:
            file.write(book + f"\n")



my_books = [
 	"Harry Potter",
 	"The Hobbit",
 	"1984",
 	"The Little Prince"
 ]

save_books(my_books)
print()

#2
with open("products.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product","price"])
    writer.writerow(["Coffee","25"])
    writer.writerow(["Tea","18"])
    writer.writerow(["Chocolate","12"])

#def read_products(filename):
#    with open(filename, "r") as file:

import csv

def read_products(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")

read_products('products.csv')

#3
import json

def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }
    with open('user.json', 'w', encoding='utf-8') as file:
        json.dump(user, file, indent=2, ensure_ascii=False)

save_user("anna21", "anna@example.com", "Israel")

#4
from pathlib import Path


def create_logs_folder():
    # 1. Создаём папку logs
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # 2. Создаём внутри неё файл app.txt и записываем строку
    file_path = logs_dir / "app.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Application started successfully!")

create_logs_folder()