import customtkinter as ctk
import generate
from customtkinter import CTkFont
from PIL import Image
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")
root=ctk.CTk()
root.geometry("600x600")
root.title("Password Manager")


sub=ctk.CTkLabel(root,text='Welcome To password Manager',font=("Times Roman",24))
sub.pack(pady=40)
class generate_button():
    def __add__(self, length):
        if addtext:
         generate.generate_ob()
generate_button()
generate_but=ctk.CTkButton(root,text="Want To Generate a Password",text_color="white",fg_color="blue")
addtext=ctk.CTkTextbox(root)
addtext.pack()
class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
   my= MyFrame()
check=ctk.CTkButton(root,text="To Check Your Paasword",text_color="white",fg_color="blue")

manage=ctk.CTkButton(root,text="Manage Your Passwords",text_color="white",fg_color="blue")
check.pack(pady=20)
manage.pack(pady=20)
my_image = ctk.CTkImage(light_image=Image.open("Image.png"),
                                  dark_image=Image.open("Image.png"),
                                  size=(360, 500))


image_label = ctk.CTkLabel(root, image=my_image, text="")
image_label.pack(pady=40)
root.mainloop()