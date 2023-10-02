import random
from tkinter import *
from tkinter import ttk

class PG:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator Application")
        self.root.geometry('600x250+300+150')

        self.label = Label(self.root, text='Password Generator App', font='Arial 25 bold',
                           width=10, bd=5, bg='light blue', fg='red')
        self.label.pack(side='top', fill='both')

        self.label2 = Label(self.root, text="Enter Length of Password", font='Arial 14 bold',
                            width=17, bd=5, bg='white', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text="Generated Password", font='Arial 18 bold',
                            width=13, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=5, bd=5, width=23, font='Arial 20 bold')
        self.main_text.place(x=280, y=100)

        self.side_text = Entry(self.root, bd=5, font='Arial 10 bold', width=10)
        self.side_text.place(x=80, y=120)

        self.button = Button(self.root, text="Generate", font='Arial 20 bold', width=10,
                             bd=5, bg='orange', fg='black', command=self.Generate)
        self.button.place(x=40, y=180)

    def Generate(self):
        import string
        plen = int(self.side_text.get())
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        password = ''.join(random.sample(s, plen))
        self.main_text.delete(0, END)
        self.main_text.insert(END, password)

root = Tk()
ui = PG(root)
root.mainloop()
