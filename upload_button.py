import tkinter as tk 
from tkinter import filedialog

def upload_file():
    filename = filedialog.askopenfile()
    print("Selected File :" ,filename)
    root.destroy()
root = tk.Tk()
root.title("File Uploader")

upload_button = tk.Button(root, text = "Upload File" , command =upload_file)
upload_button.pack()

root.mainloop()
