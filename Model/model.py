import datetime # untuk membaca waktu
import hashlib # untuk menyimpan password
import os # untuk command clear screen
import time #untuk command sleep

def clear_screen(): # untuk membersihkan terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class User: # untuk empat menyimpan password dan emoney
    def __init__(self, username, password, role, emoney=0):
        self.username = username
        self.password = password
        self.role = role
        self.emoney = emoney
    
    def hash_password(password):
        salt = os.urandom(16)
        return salt +hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    
    def check_password(self, password):
        salt = self.password[:16]
        stored_key = self.password[16:]
        input_key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
        return stored_key == input_key
    
    def top_up(self, amount):
        self.emoney += amount
        print(f"Berhasil! Saldo anda sekarang: Rp. {self.emoney}")
    
    def __str__(self):
        return f"User(username={self.username}, role={self.role}, emoney={self.emoney})"

class Product: # untuk menyimpan parameter product
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
    
    def __str__(self):
        return f"Product(id={self.id}, title={self.title}, price={self.price})"

class Transaksi: # untuk proses perhitungan transaksi
    def __init__(self, user, product):
        self.user = user
        self.product = product
        self.timestamp = None
        self.final_price = self.calculate_final_price()
    
    def calculate_final_price(self):
        if self.product.price >= 100000:
            print("Anda mendapat diskon 10%!")
            return self.product.price * 0.9
        return self.product.price
    
    def process_purchase(self):
        if self.user.emoney >= self.final_price:
            self.user.emoney -= self.final_price
            self.timestamp = datetime.datetime.now()
            print("Transaksi sukses!")
            time.sleep(1.0)
            clear_screen()
        else:
            print("Saldo anda tidak mencukupi!")
    
    def __str__(self):
        return f"Transaction(user={self.user.username}, product={self.product.title}, final_price=Rp {self.final_price})"