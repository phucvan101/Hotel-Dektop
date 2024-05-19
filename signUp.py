import tkinter as tk
import mysql.connector # thư viện chính thứ của mysql và tối ưu hóa nhất -> cần sử dụng tính năng cao hoặc hiệu suất cao
from tkinter import messagebox 
from tkinter import *
import pymysql # thư viện thuần túy của python, dễ cài đặt và sử dụng

def clear():
    email.delete(0, END)
    email.insert(0, 'Email')
    user.delete(0, END)
    user.insert(0, 'Username')
    password.delete(0, END)
    password.insert(0, 'Password')
    passwordC.delete(0, END)    
    passwordC.insert(0, 'Confirm Password')
    valueCheck.set(0)

#connection 
def connectDatabase():
    if email.get() == '' or user.get() == '' or password.get() == '' or passwordC.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif password.get() != passwordC.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif valueCheck.get() == 0:
        messagebox.showerror('Error', 'Pleased Accept Terms & Condition')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Phuc1012004@')
            cur = con.cursor()
            
            # Create database if it does not exist
            cur.execute('CREATE DATABASE IF NOT EXISTS userdata')
            cur.execute('USE userdata')
            
            # Create table if it does not exist
            cur.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
                    email VARCHAR(50), 
                    username VARCHAR(100), 
                    password VARCHAR(20)
                )
            ''')
            select_query = 'SELECT * FROM data where username=%s'
            cur.execute(select_query, (user.get()))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Username Already Exits')
            else:
                # Insert user data into the table
                insert_query = 'INSERT INTO data (email, username, password) VALUES (%s, %s, %s)'
                cur.execute(insert_query, (email.get(), user.get(), password.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration Successful')
                clear()
                signUp.destroy()
                import login
                
            
        except pymysql.MySQLError as e:
            messagebox.showerror('Error', f'Database Connection Issue: {e}')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
        

def loginPage():
    signUp.destroy()
    import login
 
signUp = Tk()
signUp.title('Login')
signUp.geometry('925x500+300+200')
signUp.configure(bg='#fff')
signUp.resizable(False, False)

img = PhotoImage(file='login1.png')
Label(signUp, image=img, bg='white').place(x = 50, y = 50)

frame=Frame(signUp, width=350, height=350, bg="white")
frame.place(x=480, y=50)

heading=Label(frame, text='Register', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=110, y=5)

#Email

def on_enter_email(e):
    email.delete(0, 'end')
    
def on_leave_email(e):
    emailC = email.get()
    if emailC == '':
        email.insert(0, "Email")

email = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
email.place(x=30, y=65)
email.insert(0, 'Email')
email.bind('<FocusIn>', on_enter_email)
email.bind('<FocusOut>', on_leave_email)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=90)

# userName
def on_enter_user(e):
    user.delete(0, 'end')
    
def on_leave_user(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
user.place(x=30, y=100)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=125)

#password
def on_enter_password(e):
    password.delete(0, 'end')
    
def on_leave_password(e):
    passW = password.get()
    if passW == '':
        password.insert(0, "Password")

password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
password.place(x=30, y=135)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter_password)
password.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=160)

# confirm password
def on_enter_passwordC(e):
    passwordC.delete(0, 'end')
    
def on_leave_passwordC(e):
    passW = passwordC.get()
    if passW == '':
        passwordC.insert(0, "Confirm Password")

passwordC = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 12))
passwordC.place(x=30, y=170)
passwordC.insert(0, 'Confirm Password')
passwordC.bind('<FocusIn>', on_enter_passwordC)
passwordC.bind('<FocusOut>', on_leave_passwordC)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=195)


# check conditions
valueCheck = IntVar()

check = Checkbutton(
    frame, 
    text='I agree to the Terms & Conditions',
    font=('Microsoft YaHei UI Light', 9, 'bold'), 
    fg='#57a1f8', 
    bg='white', 
    activebackground='white',
    activeforeground='#57a1f8', #màu của trạng thái click
    cursor='hand2',
    variable=valueCheck
                    )
check.place(x=25, y=210)



########################################################################

btSignIn = Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=connectDatabase).place(x=35, y=250)

labelQuestion = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
labelQuestion.place(x=75, y=310)

logIn = Button(frame, width=6, text='Log in', border=0, bg='white',font=('Microsoft YaHei UI Light', 9, 'bold underline'), cursor='hand2', fg='#57a1f8', activebackground='white', activeforeground='#57a1f8', command=loginPage) #curson thay đổi con trỏ chuột
logIn.place(x=215, y=310)

signUp.mainloop()