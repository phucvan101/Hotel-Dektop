from tkinter import *

def print_value():
    print(v.get())

root = Tk()
root.title("Gender Selection")

# Tạo biến StringVar để lưu trữ giá trị của nút radio được chọn
v = StringVar()
v.set("male")  # Đặt giá trị mặc định

# Tạo các nút radio
Radiobutton(root, text='Male', variable=v, value="male").pack(anchor=W)
Radiobutton(root, text='Female', variable=v, value="female").pack(anchor=W)

# Thêm nút để in giá trị của biến v
Button(root, text='Print Value', command=print_value).pack(anchor=W)

root.mainloop()
