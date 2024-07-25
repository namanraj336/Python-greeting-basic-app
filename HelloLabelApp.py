from tkinter import *
import os
os.system('cls')
root = Tk()
root.title('learning python')
root.geometry("400x400")

def hello():
    hello_label= Label(root, text= "Hello " + myTextbox.get())
    hello_label.pack()

myLabel = Label(root, text= "Enter your first name:")
myLabel.pack()

myTextbox = Entry(root, width=50)
myTextbox.pack()

myButton = Button(root, text="Submit", command=hello)
myButton.pack()

root.mainloop()