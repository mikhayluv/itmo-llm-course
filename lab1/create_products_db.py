import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("products.db")

PRODUCTS = [
    (1, "Lenovo IdeaPad 3", "laptop", 45000),
    (2, "ASUS Vivobook 15", "laptop", 55000),
    (3, "Acer Aspire 5", "laptop", 65000),
    (4, "HP Pavilion 15", "laptop", 85000),
    (5, "Apple MacBook Air", "laptop", 120000),
    (6, "Xiaomi Redmi Note 13", "smartphone", 18000),
    (7, "Samsung Galaxy A35", "smartphone", 28000),
    (8, "Google Pixel 8a", "smartphone", 45000),
    (9, "Samsung Galaxy S24", "smartphone", 75000),
    (10, "Apple iPhone 15", "smartphone", 90000),
    (11, "Lenovo Tab M11", "tablet", 15000),
    (12, "Samsung Galaxy Tab A9", "tablet", 22000),
    (13, "Xiaomi Pad 6", "tablet", 29000),
    (14, "Apple iPad", "tablet", 45000),
    (15, "Samsung Galaxy Tab S9", "tablet", 70000),
]


def create_database():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL CHECK (
                    category IN ('laptop', 'smartphone', 'tablet', 'other')
                ),
                price INTEGER NOT NULL CHECK (price >= 0)
            )
        """)
        connection.executemany(
            "INSERT OR IGNORE INTO products (id, name, category, price) "
            "VALUES (?, ?, ?, ?)",
            PRODUCTS,
        )
    print(f"База данных: {DB_PATH}")


if __name__ == "__main__":
    create_database()
