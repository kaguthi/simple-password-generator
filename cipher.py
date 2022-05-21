#creating password generator gui using tkinter
from tkinter import *
import random
import string

root = Tk()
root.title('Password Generator')
root.resizable(width=False, height=False)

#creating the function to generator password randomly
def generate():
	letters = string.ascii_letters
	digits = string.digits

	punctuation = string.punctuation

	characters = letters + digits + punctuation

	password = random.choices(characters, k=12)
	global passwords
	passwords = "".join(password)
	my_entry.delete(0, END)
	my_entry.insert(0, passwords)

#label 
my_label = Label(root, text="PASSWORD GENERATOR")
my_label.grid(row=0, column=0)

#entry widget
my_entry = Entry(root, width=30)
my_entry.grid(row=1, column=0, columnspan=2)

#create button
my_button = Button(root, text="Generate", command=generate)
my_button.grid(row=2, column=0, ipadx=50)	

root.mainloop()

