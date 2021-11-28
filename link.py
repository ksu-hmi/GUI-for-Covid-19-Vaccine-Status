from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
my_label = HTMLLabel(root, html="<a href='https://www.cvs.com/immunizations/covid-19-vaccine'>schedule your vaccine today! </a>")
my_label.pack(pady=20, padx=20)

root.mainloop()