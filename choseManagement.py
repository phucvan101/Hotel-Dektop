import tkinter as tk
from tkinter import *
window = Tk()
window.title('Select Management Object')
                    
window.geometry(f'400x200+600+300')
window.configure(bg='#fff')
window.grid()

def manageCustomer():
    import main 
    
def manageEmployee():
    import admin
    

btManageCus = Button(
    window, 
    text='Customer',
    bg='#57a1f8', 
    fg='white', 
    font=('Microsoft YaHei UI Light', 16, 'bold'),
    border=0,
    command=manageCustomer,
).grid(row=0, column = 0,padx=53, pady=70)
btManageEmp = Button(
    window,
    text='Employee',
    bg='#57a1f8', 
    fg='white', 
    font=('Microsoft YaHei UI Light', 16, 'bold'),
    border=0,
    command=manageEmployee,
).grid(row=0, column = 1,padx=5, pady=70)

window.mainloop()