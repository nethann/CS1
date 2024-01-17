import pyshorteners
from tkinter import * 
from tkinter import ttk


long_url = "https://www.askpython.com/python/examples/url-shortener"
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=short_url).grid(column=0, row=0)
# ttk.Button(frm, text="Copy URL")
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Entry(frm).grid(column=2, row = 0)
root.mainloop()
 
print("The Shortened URL is: " + short_url)
