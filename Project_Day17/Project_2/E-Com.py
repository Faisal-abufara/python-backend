import sqlite3
from typing import List, Tuple


class Product:
    def __init__(self, name: str, price: float, stock: int, product_id: int = None):
        self._name = name
        self._price = price
        self._stock = stock
        self._product_id = product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock

    @property
    def product_id(self) -> int:
        return self._product_id

    def update_stock(self, quantity: int):
        if quantity < 0 and abs(quantity) > self._stock:
            raise ValueError("Insufficient stock")
        self._stock += quantity


class User:
    def __init__(self, username: str, email: str, user_id: int = None):
        self._username = username
        self._email = email
        self._user_id = user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def user_id(self) -> int:
        return self._user_id


class ShoppingCart:
    def __init__(self, user: User):
        self._user = user
        self._items = {}  # Dictionary to store product_id: quantity

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > product.stock:
            raise ValueError("Not enough stock available")
        if product.product_id in self._items:
            self._items[product.product_id] += quantity
        else:
            self._items[product.product_id] = quantity

    def view_cart(self) -> List[Tuple[Product, int]]:
        return [
            (product, self._items[product.product_id])
            for product in Database().get_all_products()
            if product.product_id in self._items
        ]

    def calculate_total(self) -> float:
        total = 0.0
        db = Database()
        for product_id, quantity in self._items.items():
            product = db.get_product(product_id)
            if product:
                total += product.price * quantity
        return total

    def clear_cart(self):
        self._items.clear()


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def add_product(self, product: Product) -> int:
        self.cursor.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (product.name, product.price, product.stock),
        )
        self.conn.commit()
        product._product_id = self.cursor.lastrowid
        return product._product_id

    def get_product(self, product_id: int) -> Product:
        self.cursor.execute(
            "SELECT id, name, price, stock FROM products WHERE id = ?", (product_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return Product(row[1], row[2], row[3], row[0])
        return None

    def update_product(self, product: Product):
        self.cursor.execute(
            "UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?",
            (product.name, product.price, product.stock, product.product_id),
        )
        self.conn.commit()

    def delete_product(self, product_id: int):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def get_all_products(self) -> List[Product]:
        self.cursor.execute("SELECT id, name, price, stock FROM products")
        return [
            Product(row[1], row[2], row[3], row[0]) for row in self.cursor.fetchall()
        ]

    def add_user(self, user: User) -> int:
        self.cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (user.username, user.email),
        )
        self.conn.commit()
        user._user_id = self.cursor.lastrowid
        return user._user_id

    def get_user(self, user_id: int) -> User:
        self.cursor.execute(
            "SELECT id, username, email FROM users WHERE id = ?", (user_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return User(row[1], row[2], row[0])
        return None

    def checkout(self, cart: ShoppingCart):
        db = Database()
        for product_id, quantity in cart._items.items():
            product = db.get_product(product_id)
            if not product or product.stock < quantity:
                raise ValueError(f"Insufficient stock for product {product_id}")
            product.update_stock(-quantity)
            db.update_product(product)
        cart.clear_cart()

    def __del__(self):
        self.conn.close()


# Example usage
if __name__ == "__main__":
    # Initialize database
    db = Database()

    # Create a user
    user = User("john_doe", "john@example.com")
    db.add_user(user)

    # Create products
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Mouse", 29.99, 50)
    db.add_product(product1)
    db.add_product(product2)

    # Create a shopping cart
    cart = ShoppingCart(user)
    cart.add_product(product1, 2)
    cart.add_product(product2, 3)

    # View cart
    print("Cart contents:")
    for product, quantity in cart.view_cart():
        print(f"{product.name}: {quantity} x ${product.price}")

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Checkout
    db.checkout(cart)
    print("Checkout complete. Cart cleared.")
    print(
        f"Updated stock for {product1.name}: {db.get_product(product1.product_id).stock}"
    )
    print(
        f"Updated stock for {product2.name}: {db.get_product(product2.product_id).stock}"
    )
