import functions


while True:
    user = input("""1.Want To Generate a Password 
    2.To Check Your Paasword
    3.Manage Your Passwords:  """ )
    if user == "1":
        password = functions.generate()
        save_password = input("You Want To Save This Password (Yes/No):")
        if "yes" in save_password:
              reason = input("what purpose your saving this password:")
              store=(f"{reason}-{password}")
              functions.save_password(store+"\n")
    elif user == "2":
         functions.to_check()
    elif user=="3":
        functions.manage_password()
        c = pd.read_csv("data.csv",index_col=False)
        print(pd.DataFrame(c))

