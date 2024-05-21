import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tab Switching Example")
root.geometry("400x300")

# Tạo một Notebook
notebook = ttk.Notebook(root)

# Tạo các frame cho các tab khác nhau
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Thêm các frame vào Notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Hiển thị Notebook
notebook.pack(expand=True, fill="both")

# Thêm nội dung vào Tab 1
label1 = tk.Label(tab1, text="This is Tab 1", font=("Arial", 18))
label1.pack(pady=20)

# Thêm nội dung vào Tab 2
label2 = tk.Label(tab2, text="This is Tab 2", font=("Arial", 18))
label2.pack(pady=20)

# Tạo nút để chuyển đến Tab 2 từ Tab 1
def switch_to_tab2():
    notebook.select(tab2)

button1 = tk.Button(tab1, text="Go to Tab 2", command=switch_to_tab2)
button1.pack(pady=10)

# Tạo nút để chuyển đến Tab 1 từ Tab 2
def switch_to_tab1():
    notebook.select(tab1)

button2 = tk.Button(tab2, text="Go to Tab 1", command=switch_to_tab1)
button2.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
