import tkinter as tk
import customtkinter as ctk
from windows.widgets.rtk_button import RTkButton
from windows.widgets.rtk_entry import RTkEntry
def clicked():
    print('Clicked !')

root = tk.Tk()
root.configure()

ctk.set_appearance_mode("light")

button = RTkButton(root, command=clicked)
button.pack(pady=5)

button2 = tk.Button(root, text='Button', relief=tk.SUNKEN).pack(pady=5)

entry = RTkEntry(root, relief='flat')
entry.pack(pady=5)

entry2 = tk.Entry(root, relief=tk.SUNKEN)
entry2.pack(pady=5)

entry3 = ctk.CTkEntry(root, placeholder_text='Entry').pack(pady=5)

root.mainloop()