import tkinter as tk

root = tk.Tk()
root.title("Test GUI")
root.geometry("300x200")

label = tk.Label(root, text="Hello, World!")
label.pack(pady=50)

root.mainloop()
