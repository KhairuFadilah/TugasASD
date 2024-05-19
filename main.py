from Controller.controller import UserController
from Controller.controller import ProductController
from Controller.controller import TransaksiController
from Model.model import User
from Model.model import Product
from View.view import View

def main():
    users = []
    products = []
    transactions = []
    
    admin_password = "admin_miku"
    hashed_password = User.hash_password(admin_password)
    admin_user = User("admin", hashed_password, "admin", 0)
    users.append(admin_user)
    
    customer_password = "customer_miku"
    customer_hashed_password = User.hash_password(customer_password)
    customer_user = User("customer", customer_hashed_password, "customer", 0)
    users.append(customer_user)
    
    products.append(Product("G001", "Grand Theft Auto V: Premium Edition", 153600))
    products.append(Product("G002", "MotoGP™24", 699000))
    products.append(Product("G003", "Call of Duty®: Modern Warfare® III", 1050000))
    products.append(Product("G004", "FC 24", 759000))
    products.append(Product("G005", "DreadOut", 19199))
    products.append(Product("G006", "Manny's", 74000))
    
    user_controller = UserController(users)
    product_controller = ProductController(products)
    transaksi_controller = TransaksiController(transactions)
    
    view = View(user_controller, product_controller, transaksi_controller)
    
    view.display_menu()

if __name__ == "__main__":
    main()