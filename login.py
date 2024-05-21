import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pymysql


def forgetPassword():
    login.destroy()
    import forgetPassword


def loginUser():
    if user.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Phuc1012004@', database='userdata')
            cur = con.cursor()
            if user.get() == 'admin' and password.get() == 'admin123456':
                dbName = 'admin'
                query = f'SELECT * FROM {dbName} WHERE userName=%s AND password=%s'
                cur.execute(query, (user.get(), password.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror('Error', 'Invalid username or password')
                else:
                    login.destroy()
                    import choseManagement
            else: 
                dbName = 'employee'
                query = f'SELECT * FROM {dbName} WHERE userName=%s AND password=%s'
                cur.execute(query, (user.get(), password.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror('Error', 'Invalid username or password')
                else:
                    login.destroy()
                    import main
        except pymysql.MySQLError as e:
            messagebox.showerror('Error', f'Error executing query: {e}')
        finally:
            con.close()
 
login = Tk()
login.title('Login')
login.geometry('925x500+300+200')
login.configure(bg='#fff')
login.resizable(False, False)

img = PhotoImage(file='login1.png')
Label(login, image=img, bg='white').place(x = 50, y = 50)

frame=Frame(login, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Log In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=5)
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
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

########----------------------------------------------------------------
def on_enter_password(e):
    password.delete(0, 'end')
    
def on_leave_password(e):
    passW = password.get()
    if passW == '':
        password.insert(0, "Password")

def hide():
    openEye.config(file='cE.png')
    password.config(show="*")
    eyeButton.config(command=show)

def show():
    openEye.config(file='oE.png')
    password.config(show="")
    eyeButton.config(command=hide)

password = Entry(
    frame, 
    width=25, 
    fg='black', 
    border=0, 
    bg='white', 
    font=('Microsoft YaHei UI Light', 12)
)
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter_password)
password.bind('<FocusOut>', on_leave_password)

openEye = PhotoImage(file='oE.png')
eyeButton = Button(
    frame, 
    image=openEye, 
    bd=0,
    bg='white', 
    activebackground='white',
    cursor='hand2', 
    command=hide
).place(x= 290, y = 150)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Forget password
forgetButton = Button(
    frame, 
    text='Forget Password?', 
    bd=0, bg='white', 
    activebackground='white', 
    cursor='hand2', 
    font=('Microsoft YaHei UI Light', 10), command=forgetPassword
)
forgetButton.place(x= 215, y = 183)



########################################################################

btSignIn = Button(
    frame, 
    width=39, 
    pady=7, 
    text='Sign in',
    bg='#57a1f8',
    fg='white',
    border=0,
    command=loginUser
).place(x=35, y=230)


login.mainloop()