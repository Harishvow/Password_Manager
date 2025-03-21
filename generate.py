import random as rd



def generate_ob():
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
