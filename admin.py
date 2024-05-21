from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
# connect MySQL
import mysql.connector


hotel = Tk()
hotel.title(" Management system")
hotel.geometry("1600x800+0+0") #thay đổi kích thước của cửa sổ +0+0 tương ứng với đặt nó vào vị trí góc trên trái của màn hình
        
#Main
MainFrame = Frame(hotel)
MainFrame.grid() #grid tạo lưới 
        
#Top
TopFrame = Frame(
    MainFrame, 
    bd=10, 
    width=1600, 
    height=650, 
    padx=2, 
    relief=RIDGE
).pack(side=TOP)

#Left
LeftFrame = Frame(
    TopFrame,
    bd=5, 
    width=400,
    height=650,
    relief=RIDGE
).pack(side=LEFT , anchor="w")
        

        
#Right
RightFrame = Frame(
    TopFrame,
    bd=5, 
    width=1080,
    height=650, 
    relief=RIDGE
).pack(side=RIGHT)
        

        
#Bottom
BottonFrame = Frame(
    MainFrame, 
    bd = 10, 
    width=1530, 
    height=150, 
    padx=2,
    relief=RIDGE
).pack(side=BOTTOM)
        
#===========================Variable desc====================

empId = tk.StringVar()
firstNameEmployee = tk.StringVar()
lastNameEmployee  = tk.StringVar()
addressEmployee = tk.StringVar()
dobEmployee = tk.StringVar()
mobileEmployee = tk.StringVar()
emailEmployee = tk.StringVar()
nationalEmployee = tk.StringVar()
genderEmployee = tk.StringVar()
userName = tk.StringVar()
password = tk.StringVar()
 
x = random.randint(1000, 9999)
randomRef = str(x) 
empId.set("E" + randomRef)
        
        
#================================function====================
# exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Hotel Manage System", "Confirm if you want to exit")
    if iExit > 0:
        hotel.destroy()
        return 
        
#reset
def Reset():
    firstNameEmployee.set("")
    lastNameEmployee.set("")
    addressEmployee.set("")
    dobEmployee.set("")
    mobileEmployee.set("")
    emailEmployee.set("")
    nationalEmployee.set("")
    genderEmployee.set("")
    userName.set("")
    password.set("")

            
    txtempId.delete(0, END)
    txtFirstNameEmployee.delete(0, END)
    txtLastnameEmployee.delete(0, END)
    txtAddressEmployee.delete(0, END)
    txtDOBEmployee.delete(0, END)
    txtEmailEmployee.delete(0, END)
    txtMobileEmployee.delete(0, END)
    txtNationalEmployee.delete(0, END)
    txtGenderEmployee.delete(0, END)
    txtUserName.delete(0, END)
    txtPassword.delete(0, END)
    
    x = random.randint(1000, 9999)
    randomRef = str(x) 
    empId.set("E" + randomRef)
         

            
        
# totalCostAndAdDat
def AddData():
    if firstNameEmployee.get() == '' or lastNameEmployee.get() == '' or addressEmployee.get() == '' or dobEmployee.get() == '' or mobileEmployee.get() == '' or emailEmployee.get() == '' or nationalEmployee.get() == '' or genderEmployee.get() == '' or userName.get() == '' or password.get() == '':
        tkinter.messagebox.showerror('Error', 'All Fields Are Required')
        return 
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="userdata")
        cur = sqlCon.cursor()
        sql = "INSERT INTO employee (empId, firstNameEmployee, lastNameEmployee, addressEmployee, dobEmployee, mobileEmployee, emailEmployee, nationalEmployee, genderEmployee, userName, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            empId.get(),
            firstNameEmployee.get(),
            lastNameEmployee.get(),
            addressEmployee.get(),
            dobEmployee.get(),
            mobileEmployee.get(),
            emailEmployee.get(), #
            nationalEmployee.get(),
            genderEmployee.get(),
            userName.get(),
            password.get(),       
        )    
        cur.execute(sql, data)
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Enter Successfully")
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
# Display    
def displayData():
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="userdata")
        cur = sqlCon.cursor()
        cur.execute("select empId, firstNameEmployee, lastNameEmployee, addressEmployee, dobEmployee, mobileEmployee,emailEmployee, nationalEmployee, genderEmployee, userName, password from employee")
        result = cur.fetchall() # lấy hết kết quả hàng từ truy vấn
        if len(result) != 0:
            # xóa tất cả các hàng hiện có trong treeview
            manageEmployee.delete(*manageEmployee.get_children())
                    
            # chèn lại tất cả dữ liệu đã truy vấn vào trên treeview
            for row in result:
                manageEmployee.insert('',END, values=row)
        sqlCon.commit()
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
        
# # click one Data 
def on_treeview_select(event):
    selected_item = manageEmployee.selection()[0]
    emp_id = manageEmployee.item(selected_item, 'values')[0]
    viewOne(emp_id)

        
# viewOne  
def viewOne(emp_id):
    try:
        sqlCon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Phuc1012004@",
        database="userdata"
        )
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM employee WHERE empId = %s", (emp_id,))
        row = cur.fetchone()
                
        if row:
            empId.set(row[0]),
            firstNameEmployee.set(row[1]),
            lastNameEmployee.set(row[2]),
            addressEmployee.set(row[3]),
            dobEmployee.set(row[4]),
            mobileEmployee.set(row[5]),
            emailEmployee.set(row[6]), #
            nationalEmployee.set(row[7]),
            genderEmployee.set(row[8]),
            userName.set(row[9]),
            password.set(row[10]),
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
            
# #Update
def update():
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="userdata")
        cur = sqlCon.cursor()
        # Kiểm tra sự tồn tại của empId trong cơ sở dữ liệu
        cur.execute("SELECT * FROM employee WHERE empId = %s", (empId.get(),))
        result = cur.fetchone()
        if result is None:
            tkinter.messagebox.showerror("Error", "Invalid empId. Please select a valid empId.")
            return  # Dừng chương trình khi empId không tồn tại
        cur.execute("update employee set firstnameEmployee=%s, lastnameEmployee=%s, addressEmployee=%s, dobEmployee=%s, mobileEmployee=%s, emailEmployee=%s, nationalEmployee=%s, genderEmployee=%s, userName=%s, password=%s where empId=%s", (
            firstNameEmployee.get(),
            lastNameEmployee.get(),
            addressEmployee.get(),
            dobEmployee.get(),
            mobileEmployee.get(),
            emailEmployee.get(),
            nationalEmployee.get(),
            genderEmployee.get(),
            userName.get(),
            password.get(),
            empId.get(),
        ))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record successfully updated")
            
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
    displayData()

#delete
def delete():
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="userdata")
        cur = sqlCon.cursor()
        # Kiểm tra sự tồn tại của empId trong cơ sở dữ liệu
        cur.execute("SELECT * FROM employee WHERE empId = %s", (empId.get(),))
        result = cur.fetchone()
        if result is None:
            tkinter.messagebox.showerror("Error", "Invalid empId. Please select a valid empId.")
            return  # Dừng chương trình khi empId không tồn tại
        cur.execute("DELETE FROM employee WHERE empId=%s", (empId.get(),))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record successfully delete")
    except mysql.connector.Error as err:
        tkinter.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
    displayData()
    Reset()
        
def search():
    try:
        emp_id_value = empId.get()
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="userdata")
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM employee WHERE empId=%s", (emp_id_value,))
        row = cur.fetchone()
        if row is not None:
            empId.set(row[0]),
            firstNameEmployee.set(row[1]),
            lastNameEmployee.set(row[2]),
            addressEmployee.set(row[3]),
            dobEmployee.set(row[4]),
            mobileEmployee.set(row[5]),
            emailEmployee.set(row[6]),
            nationalEmployee.set(row[7]),
            genderEmployee.set(row[8]),
            userName.set(row[9]),
            password.set(row[10]),
        else: 
            tkinter.messagebox.showinfo("Input Form", "No Record Found")
            Reset()
        sqlCon.commit()
    except:
        tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
        Reset()
    # sqlCon.close()
    finally:
        if sqlCon is not None and sqlCon.is_connected():
            cur.close()
            sqlCon.close()
        
# #tạo mã định doanh khách hàng
#===========================Widget=================
lblempId = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Employee Id:", 
    padx=1
 )
lblempId.grid(row=0, column=0, sticky=W)
txtempId = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=empId
)
txtempId.grid(row=0, column=1, pady=3, padx=40)
        
#FirstnameEmployee
lblFirstNameEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Frist Name:", 
    padx=1
)
lblFirstNameEmployee.grid(row=4, column=0, sticky=W)
txtFirstNameEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=firstNameEmployee
)
txtFirstNameEmployee.grid(row=4, column=1, pady=3, padx=40)
        
#LastnameEmployee
lblLastnameEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Last Name:", 
    padx=1
)
lblLastnameEmployee.grid(row=8, column=0, sticky=W)
txtLastnameEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=lastNameEmployee
)
txtLastnameEmployee.grid(row=8, column=1, pady=3, padx=40)
        
#Adress 
lblAddressEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Address:", 
    padx=1
)
lblAddressEmployee.grid(row=12, column=0, sticky=W)
txtAddressEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=addressEmployee
)
txtAddressEmployee.grid(row=12, column=1, pady=3, padx=40)
        
#Date of Birth
lblDOBEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Date Of Birth:", 
    padx=1
)
lblDOBEmployee.grid(row=16, column=0, sticky=W)
txtDOBEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=dobEmployee
)
txtDOBEmployee.grid(row=16, column=1, pady=3, padx=40)
        
#MobileEmployee
lblMobileEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Mobile:", 
    padx=1
)
lblMobileEmployee.grid(row=20, column=0, sticky=W)
txtMobileEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=mobileEmployee
    )
txtMobileEmployee.grid(row=20, column=1, pady=3, padx=40)
        
#EmailEmployee
lblEmailEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Email:", 
    padx=1
)
lblEmailEmployee.grid(row=24, column=0, sticky=W)
txtEmailEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=emailEmployee
)
txtEmailEmployee.grid(row=24, column=1, pady=3, padx=40)
        
#NationalEmployee
lblNationalEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="National:", 
    padx=1
)
lblNationalEmployee.grid(row=28, column=0, sticky=W)
txtNationalEmployee = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=nationalEmployee
)
txtNationalEmployee.grid(row=28, column=1, pady=3, padx=40)
        
#GenderEmployee 
lblGenderEmployee = Label(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    text="Gender:", 
    padx=1
)
lblGenderEmployee.grid(row=32, column=0, sticky=W)
txtGenderEmployee = ttk.Combobox(
    LeftFrame, 
    state='readonly', 
    font=('arial', 14, 'bold'), 
    width=17, 
    textvariable=genderEmployee
)
txtGenderEmployee ['value'] = (' ', 'Male', 'Female', 'Other')
txtGenderEmployee.current(0)
txtGenderEmployee.grid(row=32, column=1, pady=3, padx=40)
        
#username login
lblUserName = Label(
    LeftFrame,
    font=('arial', 14, 'bold'),
    text="Username login: ",
    padx=1
)
lblUserName.grid(row=36, column=0, sticky=W)
txtUserName = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=userName
)
txtUserName.grid(row=36, column=1, pady=3, padx=40)

#password
lblPassword = Label(
    LeftFrame,
    font=('arial', 14, 'bold'),
    text="Password login: ",
    padx=1
)
lblPassword.grid(row=40, column=0, sticky=W)
txtPassword = Entry(
    LeftFrame, 
    font=('arial', 14, 'bold'), 
    width=18, 
    textvariable=password
)
txtPassword.grid(row=40, column=1, pady=3, padx=40)


        

        
#====================================================widgets================================================
        
scrollbar = Scrollbar(RightFrame, orient=VERTICAL) #vertical cuộn theo hướng dọc 
manageEmployee = ttk.Treeview(
    RightFrame, 
    height=32, 
    columns=("empId", "firstNameEmployee", "lastNameEmployee", "addressEmployee", "dobEmployee", "mobileEmployee","emailEmployee", "nationalEmployee", "genderEmployee", "userName", "password"), 
    yscrollcommand=scrollbar.set
)
        
scrollbar.pack(side = RIGHT, fill=Y)
manageEmployee.heading("empId", text = "empId")
manageEmployee.heading("firstNameEmployee", text = "First Name")
manageEmployee.heading("lastNameEmployee", text = "Last Name")
manageEmployee.heading("addressEmployee", text = "Address")
manageEmployee.heading("dobEmployee", text = "Date Of Birth")
manageEmployee.heading("mobileEmployee", text = "Mobile")
manageEmployee.heading("emailEmployee", text = "Email") 
manageEmployee.heading("nationalEmployee", text = "National")
manageEmployee.heading("genderEmployee", text = "Gender")
manageEmployee.heading("userName", text = "UserName")
manageEmployee.heading("password", text = "Password")

manageEmployee['show'] = 'headings'
        
manageEmployee.column("empId", width=60)
manageEmployee.column("firstNameEmployee", width=70)
manageEmployee.column("lastNameEmployee", width=70)
manageEmployee.column("addressEmployee", width=160)
manageEmployee.column("dobEmployee", width=100)
manageEmployee.column("mobileEmployee", width=100)
manageEmployee.column("emailEmployee", width= 100)
manageEmployee.column("nationalEmployee", width=80)
manageEmployee.column("genderEmployee", width=60)
manageEmployee.column("userName", width=90)
manageEmployee.column("password", width=90)

        
manageEmployee.pack(fill= BOTH, expand=1)
manageEmployee.bind("<ButtonRelease-1>", on_treeview_select)
# displayData()
#====================================================widgets================================================
        
        
        
 #====================================================Widgets Button================================================
#Add data
btnAddData = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, height=2, 
    text="Add Data", 
    cursor='hand2', 
    bg='#57a1f8', 
    fg='white', 
    command=AddData
).grid(row=0, column=0, padx=4, pady=1)

        
#Display
btnDisplay = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, height=2, 
    text="Display",
    cursor='hand2', 
    bg='#57a1f8', 
    fg='white', 
    command=displayData
).grid(row=0, column=1, padx=4, pady=1)
        
#Update
btnUpdate = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, height=2, 
    text="Update",
    cursor='hand2', 
    bg='#57a1f8', 
    fg='white', 
    command=update
).grid(row=0,column=2, padx=4, pady=1)
        
#Search
btnSearch = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, height=2, 
    text="Search",
    cursor='hand2', 
    bg='#57a1f8', 
    fg='white', 
    command=search
).grid(row=0,column=4, padx=4, pady=1)
        
#Delete
btnDelete = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, 
    height=2, 
    text="Delete",
    cursor='hand2', 
    bg='#57a1f8', 
    fg='white', 
    command=delete
).grid(row=0,column=3, padx=4, pady=1)
        
#Reset
btnReset = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'), 
    width=15, 
    height=2, 
    text="Reset",
    cursor='hand2',
    bg='#57a1f8', 
    fg='white', 
    command=Reset
).grid(row=0,column=5, padx=4, pady=1)
        
# Exit
btnExit = Button(
    BottonFrame, 
    bd=4, 
    font=('arial', 16, 'bold'),
    width=14, height=2,
    text="Exit",cursor='hand2',
    bg='#57a1f8', 
    fg='white', 
    command=iExit
).grid(row=0,column=6, padx=4, pady=1)
        
hotel.mainloop()