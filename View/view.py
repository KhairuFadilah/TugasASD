from prettytable import PrettyTable
import os
import sys # untuk mengeluarkan program
import datetime
import time
import getpass # untuk menghilangkan inputan password

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def exit_program():
    sys.exit()

class View:
    def __init__(self, user_controller, product_controller, transaksi_controller):
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.transaksi_controller = transaksi_controller
    
    def display_menu(self):
        clear_screen()
        while True:
            current_time = datetime.datetime.now()
            if current_time.hour < 8 or current_time.hour >= 24:
                clear_screen()
                print("Mohon maaf, toko hanya beroperasi dari jam 8.00-16.00 WITA.")
                return
            
            user = self.login()
            if user is None:
                continue
            
            if user.role == "admin":
                self.admin_menu(user)
            elif user.role == "customer":
                self.customer_menu(user)
    
    def login(self):
        clear_screen()
        print("Apabila ingin Exit, silahkan mengetik 'exit' pada username atau password.")
        username = input("Masukkan username: ")
        if username.lower() == 'exit':
            print("Terima Kasih!")
            exit_program()
        password = getpass.getpass("Masukkan password: ")
        if password.lower() == 'exit':
            print("Terima Kasih!")
            exit_program()
        return self.user_controller.login(username, password)
    
    def admin_menu(self, user):
        clear_screen()
        while True:
            print("+ ------ MENU ADMIN ------ +")
            print("| 1. Tambahkan produk      |")
            print("| 2. Tampilkan Produk      |")
            print("| 3. Update produk         |")
            print("| 4. Hapus produk          |")
            print("| 5. Logout                |")
            print("| 6. Keluar Program        |")
            print("+ ------------------------ +")
            choice = input("Masukkan pilihan: ")
            if choice == "1":
                clear_screen()
                self.add_product()
            elif choice == "2":
                clear_screen()
                self.show_product()
            elif choice == "3":
                clear_screen()
                self.update_product()
            elif choice == "4":
                clear_screen()
                self.delete_products()
            elif choice == "5":
                clear_screen()
                print("Logout Berhasil! Mohon Menunggu...")
                time.sleep(1.0)
                return
            elif choice == "6":
                print("Terima Kasih!")
                exit_program()
            else:
                print("Pilihan tidak valid!")
                time.sleep(0.5)
                clear_screen()
    
    def add_product(self):
        try:
            id = input("Masukkan ID: ")
            title = input("Masukkan nama produk: ")
            price = int(input("Masukkan harga: "))
            self.product_controller.add_product(id, title, price)
            print("Produk ditambahkan!")
            time.sleep(0.5)
            clear_screen()
        except ValueError:
            print("Harga harus berupa angka!")
        
    def update_product(self):
        try:
            id = input("Masukkan ID produk yang ingin diperbaharui: ")
            title = input("Masukkan nama produk baru: ")
            price = int(input("Masukkan harga baru: "))
            self.product_controller.update_product(id, title=title, price=price)
            print("Produk diperbaharui!")
            time.sleep(0.5)
            clear_screen()
        except ValueError:
            print("Harga harus berupa angka!")
        
    def delete_products(self):
        id = input("Masukkan ID produk yang ingin dihapus: ")
        self.product_controller.delete_products(id)
        print("Produk dihapus!")
        time.sleep(0.5)
        clear_screen()
    
    def customer_menu(self, user):
        clear_screen()
        while True:
            print("+ ----------- MENU CUSTOMER ----------- +")
            print("| 1. Beli Produk                        |")
            print("| 2. Tampilkan Produk                   |")
            print("| 3. Top Up e-Money                     |")
            print("| 4. Tampilkan e-Money                  |")
            print("| 5. Cari Produk                        |")
            print("| 6. Urutkan Produk berdasarkan Harga   |")
            print("| 7. Logout                             |")
            print("| 8. Exit Program                       |")
            print("+ ------------------------------------- +")
            choice = input("Masukkan pilihan: ")
            
            if choice == "1":
                clear_screen()
                self.purchase_product(user)
            elif choice == "2":
                clear_screen()
                self.show_product()
            elif choice == "3":
                clear_screen()
                self.top_up_emoney(user)
            elif choice == "4":
                clear_screen()
                self.check_emoney(user)
            elif choice == "5":
                clear_screen()
                self.search_product()
            elif choice == "6":
                clear_screen()
                self.sort_product()
            elif choice == "7":
                clear_screen()
                print("Logout Berhasil! Mohon Menunggu...")
                time.sleep(1.0)
                return
            elif choice == "8":
                print("Terima Kasih!")
                exit_program()
            else:
                print("Pilihan tidak valid!")
                time.sleep(0.5)
                clear_screen()
    
    def search_product(self):
        search_term = input("Masukkan nama game yang ingin dicari: ")
        found_products = self.product_controller.search_products(search_term)
        if found_products:
            for product in found_products:
                table = PrettyTable()
                table.field_names = ["ID Produk", "Judul Game", "Harga"]
                for product in found_products:
                    table.add_row([product.id, product.title, product.price])
                print(table)
        else:
            print("Tidak ada produk yang cocok dengan pencarian.")
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    

    def sort_product(self):
        order = input("Urutkan harga (termurah/termahal): ")
        if order.lower() not in ['termurah', 'termahal']:
            print("Pilihan tidak valid, menggunakan urutan termurah")
            order = 'termurah'
        sorted_products = self.product_controller.sort_products(ascending=order == 'termurah')
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in sorted_products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def show_product(self):
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in self.product_controller.products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def check_emoney(self, user):
        print(f"Saldo e-Money Anda saat ini adalah: Rp {user.emoney}")
        input("Tekan enter untuk kembali ke menu utama...")
        clear_screen()
    
    def purchase_product(self, user):
        table = PrettyTable()
        table.field_names = ["ID Produk", "Judul Game", "Harga"]
        for product in self.product_controller.products:
            table.add_row([product.id, product.title, product.price])
        print(table)
        print("")
        product_id = input("Masukkan ID game yang ingin dibeli: ")
        self.transaksi_controller.process_purchase(user, product_id, self.product_controller.products)
    
    def top_up_emoney(self, user):
        try:
            amount = float(input("Masukkan jumlah yang ingin ditambahkan: "))
            if amount == 0:
                print("Saldo yang diisi tidak boleh 0!")
                time.sleep(0.5)
                clear_screen()
                return
            self.user_controller.top_up_emoney(user, amount)
            input("Tekan enter untuk kembali ke menu utama...")
            clear_screen()
        except ValueError:
            print("Inputan harus berupa angka!")