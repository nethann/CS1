from tkinter import *
from tkinter import ttk
import pyshorteners
from urllib.parse import urlparse

root = Tk()
root.geometry('400x150')
root.title("URL shortener")
root.resizable(FALSE, FALSE)

# Creating a frame to hold the elements
frame = Frame(root)
frame.pack()

entry = ttk.Entry(frame)
entry.grid(row=0, column=0, padx=0, pady=5)

label = ttk.Label(frame, text='Nethan Nagendran Productions!')
label.grid(row=1, column=0, pady=10)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_entry_value():
    # getting value from entry input
    value = entry.get()

    if is_valid_url(value):
        # generating short URL
        long_url = value
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)

        # printing out val
        print(f'Link being generated: {short_url}')

        # Copying to clipboard
        root.clipboard_clear()
        root.clipboard_append(short_url)

        label.config(text=f'{short_url}\nHas been copied to your clipboard!')
    else:
        label.config(text="Please make sure you add a VALID URL!")

generate_URL = ttk.Button(frame, text="Generate Short Url", command=get_entry_value)
generate_URL.grid(row=2, column=0, pady=5)

root.mainloop()
