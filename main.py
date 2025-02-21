import functions
from functions import save_password
while True:
    user = input("""1.Want To Generate a Password 
    2.To Check Your Paasword
    3.Manage Your Passwords:  """ )
    if user == "1":
        password = functions.generate()
        save_password = input("You Want To Save This Password (Yes/No):")
        if "yes" in save_password:
              functions.save_password(password+"\n")
    elif user == "2":
         functions.to_check()
    elif user=="3":
        functions.manage_password()

