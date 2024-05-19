import tkinter as tk
import mysql.connector 
from tkinter import messagebox
from tkinter import *
import pymysql

    
def changePassword():
    if user.get() == '' or nPassword.get() == '' or cPassword.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif nPassword.get() != cPassword.get():
        messagebox.showerror('Error', 'Password and Confirm Password are not matching', )
        
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Phuc1012004@', database='userdata')
            cur = con.cursor()
            query = 'SELECT * FROM data WHERE username=%s'
            cur.execute(query, (user.get()))
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror('Error', 'Incorrect Username')
            else:
                query = 'UPDATE data set password=%s WHERE username=%s'
                cur.execute(query, (nPassword.get(), user.get()))
                con.commit()
                messagebox.showinfo('Success', 'Password is reset, please login with new password')
                resetPassword.destroy()
                import login
        except pymysql.MySQLError as e:
            messagebox.showerror('Error', f'Error executing query: {e}')
        finally:
            con.close()
 
resetPassword = Tk()
resetPassword.title('Reset Password')
resetPassword.geometry('925x500+300+200')
resetPassword.configure(bg='#fff')
resetPassword.resizable(False, False)

img = PhotoImage(file='login1.png')
Label(resetPassword, image=img, bg='white').place(x = 50, y = 50)

frame=Frame(resetPassword, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Reset Password', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=60, y=5)
########----------------------------------------------------------------
def on_enter_user(e):
    user.delete(0, 'end')
    
def on_leave_user(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=105)

# New password
def on_enter_nPassword(e):
    nPassword.delete(0, 'end')
    
def on_leave_nPassword(e):
    passW = nPassword.get()
    if passW == '':
        nPassword.insert(0, "New Password")

nPassword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
nPassword.place(x=30, y=135)
nPassword.insert(0, 'New Password')
nPassword.bind('<FocusIn>', on_enter_nPassword)
nPassword.bind('<FocusOut>', on_leave_nPassword)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=160)

# confirm password
def on_enter_cPassword(e):
    cPassword.delete(0, 'end')
    
def on_leave_cPassword(e):
    passW = cPassword.get()
    if passW == '':
        cPassword.insert(0, "Confirm Password")

cPassword = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
cPassword.place(x=30, y=190)
cPassword.insert(0, 'Confirm Password')
cPassword.bind('<FocusIn>', on_enter_cPassword)
cPassword.bind('<FocusOut>', on_leave_cPassword)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=215)



########################################################################

btSubmit = Button(frame, width=39, pady=7, text='Submit', bg='#57a1f8', fg='white', border=0, command=changePassword).place(x=35, y=250)


resetPassword.mainloop()