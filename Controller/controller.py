from Model.model import Transaksi
from Model.model import Product
import time
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class UserController: # untuk mengatur login
    def __init__(self, users):
        self.users = users
    
    def login(self, username, password):
        user = next((user for user in self.users if user.username == username), None)
        print("Mohon Menunggu Sebentar...")
        time.sleep(0.5)
        if user and user.check_password(password):
            print("Login berhasil! Mohon Menunggu...")
            time.sleep(1.0)
            return user
        else:
            print("Username atau password salah!")
            time.sleep(1.0)
            return None
    
    def top_up_emoney(self, user, amount):
        user.top_up(amount)

class ProductController: # untuk mengatur produk 
    def __init__(self, products):
        self.products = products
    
    def add_product(self, id, title, price):
        new_product = Product(id, title, price)
        self.products.append(new_product)
    
    def update_product(self, product_id, **updates):
        product = next((prod for prod in self.products if prod.id == product_id), None)
        if product:
            product.__dict__.update(**updates)
            print(f"Produk dengan ID {product_id} telah diperbarui.")
        else:
            print("Produk tidak ditemukan!")
    
    def delete_products(self, product_id):
        self.products = [prod for prod in self.products if prod.id != product_id]
        print(f"Produk dengan ID {product_id} telah dihapus!")
    
    def search_products(self, search_term):
        return [prod for prod in self.products if search_term in prod.title]

    def sort_products(self, ascending=True):
        return sorted(self.products, key=lambda prod: prod.price, reverse=not ascending)

class TransaksiController: # untuk mengatur transaksi
    def __init__(self, transactions):
        self.transactions = transactions
    
    def process_purchase(self, user, product_id, products):
        product = next((prod for prod in products if prod.id == product_id), None)
        if product:
            transaction = Transaksi(user, product)
            if transaction.final_price <= user.emoney:
                transaction.process_purchase()
                self.transactions.append(transaction)
            else:
                print("Saldo E-money tidak cukup!")
                time.sleep(0.5)
                clear_screen()
        else:
            print("Produk tidak ditemukan!")
            time.sleep(0.5)
            clear_screen()