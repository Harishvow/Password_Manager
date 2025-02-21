import random as rd



def generate():
 while True:
     password="0"
     length=int(input("enter the length:"))
     if length >=8:
          example = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%^&*"
          for _ in range(length):
               password += rd.choice(example)

          print("Generated Password:", password)
          st = ""
          d = 0
          while d < 4:
               st += str(rd.randint(0, 9))
               d += 1
          sp = ""
          symbols = ["!", "@", "#", "$", "^", "&", "*"]
          p = 0
          while p < 3:
               sp += str(rd.choice(symbols))
               p += 1
          upp = ""
          character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
          u = 0
          while u < 4:
               upp += str(rd.choice(character))
               u += 1
          last = st + sp + upp

          s = ""
          for _ in last:
               s += rd.choice(last)
          return password
     else:
          print("Password length must be at least 8 characters. Please try again.")



def save_password(password):
    fun = read_passwords()
    with open("savepass.txt", "w") as file:
       fun.append(password + "\n")
       file.writelines(fun)
       print("Password saved successfully!")
def read_passwords():
    with open("savepass.txt","r") as file:
        return file.readlines()
def write_password():
    with open("savepass.txt", "w") as file:
        file.writelines("savepass.txt")



def to_check():
    password = input("Enter the password: ")
    final = {}

    if len(password) > 8:
        final["length"] = True
    else:
        final["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    final["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    final["uppercase"] = uppercase

    if all(final.values()):
        print("Your password is strong.")

    else:
        print("Your password is weak. Please try again.")
    user=input("you want to save this password yes or no :")
    if user.startswith("yes"):
        save_password(password)
        print("your password has been saved")
    else:
       print("your password has been Not saved")
def manage_password():
     ask=input("""1.Want To Show Your Passwords 
     2.Want to Delete Your Password 
     3.Want To Edit Your Password:""")
     if ask=="1":
         show=read_passwords()
         for index,item in enumerate(show):
             row=f"{index + 1}-{item.strip()}"
             print(row)
     elif ask=="2":
         read = read_passwords()
         number=int(input("Enter The Password Number:"))
         index=number-1
         remove_password=read.pop(index).strip("\n")
         with open("savepass.txt", "w") as file:
             file.writelines(read)

         msg=f"{remove_password} this Password Has been Delete"
         print(msg)
     elif ask=="3":
         asker=input("1.Edit yourself 2.want to generate")
         if asker=="1":
             read = read_passwords()
             user=int(input("enter a number want to edit :"))
             number=user-1
             new_password=input("enter a new password:")
             read[number]=new_password +"\n"
             with open("savepass.txt", "w") as file:
                 file.writelines(read)
             print("your password has been updated suceessfully")
         else:
             read = read_passwords()
             user = int(input("enter a number want to edit :"))
             number = user - 1
             new_password=generate()
             read[number] = new_password + "\n"
             with open("savepass.txt", "w") as file:
                 file.writelines(read)
             print("your password has been updated suceessfully")












