from tkinter import PhotoImage

import customtkinter as ctk
from customtkinter import CTkImage, CTkLabel

import generate

root=ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
root.geometry("600x600")
root.title("Password Manager")
sub = ctk.CTkLabel(root, text='Welcome To password Manager', font=("Times Roman", 24))
sub.pack(pady=40)
but_dic={}
words=["Want To generate Password","Want To Check Password ","Want To Manage Your Passwords"]
for i in words:
    but_dic[i]=ctk.CTkButton(root,text=i)
    but_dic[i].pack(pady=20)
root.mainloop()