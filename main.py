from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
# connect MySQL
import mysql.connector
import datetime
import time
from datetime import datetime


hotel = Tk()
hotel.title("Hotel Database Management system")
hotel.geometry("1600x800+0+0") #thay đổi kích thước của cửa sổ +0+0 tương ứng với đặt nó vào vị trí góc trên trái của màn hình
        
#Main
MainFrame = Frame(hotel)
MainFrame.grid() #grid tạo lưới 
        
#Top
TopFrame = Frame(MainFrame, bd=10, width=1600, height=650, padx=2, relief=RIDGE) #relief kiểu cài đặt viền
TopFrame.pack(side=TOP)

#Left
LeftFrame = Frame(TopFrame, bd=5, width=400, height=400, relief=RIDGE)
LeftFrame.pack(side=LEFT , anchor="w")
        

        
#Right
RightFrame = Frame(TopFrame, bd=5, width=1080, height=650, relief=RIDGE)
RightFrame.pack(side=RIGHT)
        
RightFrame2 = Frame(RightFrame, bd = 5, width=1050, height=200, padx=3, relief=RIDGE)
RightFrame2.grid(row=0, column=0)
RightFrame3 = Frame(RightFrame, bd = 5, width=1050, height=300, padx=4, relief=RIDGE)
RightFrame3.grid(row=3, column=0)
        
#Bottom
BottonFrame = Frame(MainFrame, bd = 10, width=1530, height=150, padx=2, relief=RIDGE)
BottonFrame.pack(side=BOTTOM)
        
#===========================Variable desc====================

cusID = tk.StringVar()
firstName = tk.StringVar()
lastName  = tk.StringVar()
address = tk.StringVar()
dob = tk.StringVar()
mobile = tk.StringVar()
email = tk.StringVar()
national = tk.StringVar()
gender = tk.StringVar()
dateIn = tk.StringVar()
dateOut = tk.StringVar()
typeOfId = tk.StringVar()
typeOfRoom = tk.StringVar()
roomOrder = tk.StringVar() # số thứ tự phòng của một tầng
numberFloor = tk.StringVar() # số tầng
service = tk.StringVar()
totalDays = tk.StringVar()
paidTax = tk.StringVar()
subTotal = tk.StringVar()
totalCost = tk.StringVar()
        
# tạo biến số phòng
roomN = tk.StringVar()
 
# thiết lập định dạng ngày
dateIn.set(time.strftime("%d/%m/%Y"))
dateOut.set(time.strftime("%d/%m/%Y"))
        
x = random.randint(1000, 9999)
randomRef = str(x) 
cusID.set("HT" + randomRef)
        
        
#================================function====================
# exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Hotel Manage System", "Confirm if you want to exit")
    if iExit > 0:
        hotel.destroy()
        return 
        
#reset
def Reset():
    typeOfId.set("")
    typeOfRoom.set("")
    roomOrder.set("")
    numberFloor.set("")
    service.set("")
    roomN.set("")
    totalDays.set("")
    paidTax.set("")
    subTotal.set("")
    totalCost.set("")

            
    # txtCusID.delete(0, END)
    txtFristname.delete(0, END)
    txtLastname.delete(0, END)
    txtAddress.delete(0, END)
    txtDOB.delete(0, END)
    txtEmail.delete(0, END)
    txtMobile.delete(0, END)
    txtNational.delete(0, END)
    txtGender.delete(0, END)
            
    x = random.randint(1000, 9999)
    randomRef = str(x) 
    cusID.set("HT" + randomRef)
         
# tính tổng tiền     
def valueTotalCost():
    dateIn_v = dateIn.get()
    dateOut_v = dateOut.get()
    inDate = datetime.strptime(dateIn_v, "%d/%m/%Y")
    outDate = datetime.strptime(dateOut_v, "%d/%m/%Y")
    totalDays.set(abs(outDate - inDate).days)        
    #single and service:
    if (typeOfRoom.get() == "Single" and service.get() == "Yes"):
        t1 = float(30) # giá phòng single
        t2 = float(10) # giá dịch vụ 
        t3 = float(totalDays.get())
        t12 = float(t1 + t2)
        t = float(t3 * t12)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)
                
    #single and not service 
    elif (typeOfRoom.get() == "Single" and service.get() == "No"):
        t1 = float(30) # giá phòng single
        t3 = float(totalDays.get())
        t = float(t3 * t1)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                    
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)
            
    #double and service
    elif (typeOfRoom.get() == "Double" and service.get() == "Yes"):
        t1 = float(50) # giá phòng single
        t2 = float(10) # giá dịch vụ 
        t3 = float(totalDays.get()) 
        t12 = float(t1 + t2)
        t = float(t3 * t12)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)
            
    # double and not service
    elif (typeOfRoom.get() == "Double" and service.get() == "No"):
        t1 = float(50) # giá phòng single 
        t3 = float(totalDays.get()) 
        t = float(t3 * t1)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)
            
            
    #family and service
    elif (typeOfRoom.get() == "Family" and service.get() == "Yes"):
        t1 = float(60) # giá phòng single
        t2 = float(10) # giá dịch vụ 
        t3 = float(totalDays.get()) 
        t12 = float(t1 + t2)
        t = float(t3 * t12)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)

    #family and not service
    else:
        t1 = float(60) # giá phòng single
        t3 = float(totalDays.get()) 
        t = float(t3 * t1)
        tax = "$" + str('%.2f'%((t) * 0.90)) # giá trị của thuế
        st = "$" + str('%.2f'%(t)) # giá chưa tính thuế
        tt = "$" + str('%.2f'%((t) + ((t) * 0.90))) # giá tính cả thuế 
                
        paidTax.set(tax)
        subTotal.set(st)
        totalCost.set(tt)

# Room Number       
def roomNumber():
    r = roomOrder.get()
    n = numberFloor.get()
    rN = n + r
    roomN.set(rN)
            
        
# totalCostAndAdDat
def totalCostAndAddData():
    valueTotalCost()
    roomNumber()
    if (mobile.get() == "" or service.get() == "" or typeOfRoom.get() == "" or numberFloor.get() == "" or roomOrder.get() == ""):
        tkinter.messagebox.showerror("Provide number phone,  and service")
        return 
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="hotel_management")
        cur = sqlCon.cursor()
        sql = "INSERT INTO hotel2 (cusID, firstName, lastName, address, dob, mobile, email, national, gender, dateIn, dateOut,typeOfId, typeOfRoom, roomOrder, numberFloor, service, roomN, totalDays, paidTax, subTotal, totalCost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            cusID.get(),
            firstName.get(),
            lastName.get(),
            address.get(),
            dob.get(),
            mobile.get(),
            email.get(), #
            national.get(),
            gender.get(),
            dateIn.get(),
            dateOut.get(),
            typeOfId.get(), #
            typeOfRoom.get(), #
            roomOrder.get(), #
            numberFloor.get(), #
            service.get(), #
            roomN.get(),
            totalDays.get(),
            paidTax.get(),
            subTotal.get(),
            totalCost.get()
        )    
        cur.execute(sql, data)
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Enter Successfully")
    except mysql.connector.Error as err:
        tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
# Display    
def displayData():
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="hotel_management")
        cur = sqlCon.cursor()
        cur.execute("select cusID, firstName, lastName, address, dob, mobile, national, gender, dateIn, dateOut, roomN, totalCost from hotel_management.hotel2 order by dateIn")
        result = cur.fetchall() # lấy hết kết quả hàng từ truy vấn
        if len(result) != 0:
            # xóa tất cả các hàng hiện có trong treeview
            manageHotel.delete(*manageHotel.get_children())
                    
            # chèn lại tất cả dữ liệu đã truy vấn vào trên treeview
            for row in result:
                manageHotel.insert('',END, values=row)
        sqlCon.commit()
    except mysql.connector.Error as err:
        tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
        
# click one Data 
def on_treeview_select(event):
    selected_item = manageHotel.selection()[0]
    cus_id = manageHotel.item(selected_item, 'values')[0]
    viewOne(cus_id)

        
# viewOne  
def viewOne(cus_id):
    try:
        sqlCon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Phuc1012004@",
        database="hotel_management"
        )
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM hotel_management.hotel2 WHERE cusID = %s", (cus_id,))
        row = cur.fetchone()
                
        if row:
            cusID.set(row[0]),
            firstName.set(row[1]),
            lastName.set(row[2]),
            address.set(row[3]),
            dob.set(row[4]),
            mobile.set(row[5]),
            email.set(row[6]), #
            national.set(row[7]),
            gender.set(row[8]),
            dateIn.set(row[9]),
            dateOut.set(row[10]),
            typeOfId.set(row[11]), #
            typeOfRoom.set(row[12]), #
            roomOrder.set(row[13]), #
            numberFloor.set(row[14]), # 
            service.set(row[15]), #  
            roomN.set(row[16]),
            totalDays.set(row[17]),
            paidTax.set(row[18]),
            subTotal.set(row[19]),
            totalCost.set(row[20])
    except mysql.connector.Error as err:
        tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
            
#Update
def update():
    valueTotalCost()
    roomNumber()
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="hotel_management")
        cur = sqlCon.cursor()
        # Kiểm tra sự tồn tại của cusID trong cơ sở dữ liệu
        cur.execute("SELECT * FROM hotel_management.hotel2 WHERE cusID = %s", (cusID.get(),))
        result = cur.fetchone()
        if result is None:
            tkinter.messagebox.showerror("Error", "Invalid cusID. Please select a valid cusID.")
            return  # Dừng chương trình khi cusID không tồn tại
        cur.execute("update hotel_management.hotel2 set firstname=%s, lastname=%s, address=%s, dob=%s, mobile=%s, national=%s, gender=%s, dateIn=%s, dateOut=%s,typeOfId=%s, typeOfRoom=%s, roomOrder=%s,numberFloor=%s, service=%s, totalCost=%s where cusID=%s", (
            firstName.get(),
            lastName.get(),
            address.get(),
            dob.get(),
            mobile.get(),
            national.get(),
            gender.get(),
            dateIn.get(),
            dateOut.get(),
            typeOfId.get(),
            typeOfRoom.get(),
            roomOrder.get(),
            numberFloor.get(),
            service.get(),
            totalCost.get(),
            cusID.get(),
        ))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record successfully updated")
            
    except mysql.connector.Error as err:
        tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
    displayData()

#delete
def delete():
    try:
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="hotel_management")
        cur = sqlCon.cursor()
        # Kiểm tra sự tồn tại của cusID trong cơ sở dữ liệu
        cur.execute("SELECT * FROM hotel_management.hotel2 WHERE cusID = %s", (cusID.get(),))
        result = cur.fetchone()
        if result is None:
            tkinter.messagebox.showerror("Error", "Invalid cusID. Please select a valid cusID.")
            return  # Dừng chương trình khi cusID không tồn tại
        cur.execute("DELETE FROM hotel_management.hotel2 WHERE cusID=%s", (cusID.get(),))
        sqlCon.commit()
        tkinter.messagebox.showinfo("Data Entry Form", "Record successfully delete")
    except mysql.connector.Error as err:
        tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if sqlCon.is_connected():
            cur.close()
            sqlCon.close()
    displayData()
    Reset()
        
def search():
#sear
    sqlCon = None
    try:
        valueTotalCost()
        roomNumber()
        cus_id_value = cusID.get()
        sqlCon = mysql.connector.connect(host="localhost", user="root", password="Phuc1012004@", database="hotel_management")
        cur = sqlCon.cursor()
        cur.execute("SELECT * FROM hotel_management.hotel2 WHERE cusID=%s", (cus_id_value,))
        row = cur.fetchone()
        if row is not None:
            cusID.set(row[0]),
            firstName.set(row[1]),
            lastName.set(row[2]),
            address.set(row[3]),
            dob.set(row[4]),
            mobile.set(row[5]),
            email.set(row[6]),
            national.set(row[7]),
            gender.set(row[8]),
            dateIn.set(row[9]),
            dateOut.set(row[10]),
            typeOfId.set(row[11]),
            typeOfRoom.set(row[12]),
            roomOrder.set(row[13]),
            numberFloor.set(row[14]),
            service.set(row[15]),
            roomN.set(row[16]),
            totalDays.set(row[17]),
            paidTax.set(row[18]),
            subTotal.set(row[19]),
            totalCost.set(row[20]),
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
lblCusID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Customer Ref:", padx=1)
lblCusID.grid(row=0, column=0, sticky=W)
txtCusID = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=cusID)
txtCusID.grid(row=0, column=1, pady=3, padx=40)
        
#Firstname
lblFristname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Frist Name:", padx=1)
lblFristname.grid(row=2, column=0, sticky=W)
txtFristname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=firstName)
txtFristname.grid(row=2, column=1, pady=3, padx=40)
        
#Lastname
lblLastname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Last Name:", padx=1)
lblLastname.grid(row=4, column=0, sticky=W)
txtLastname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=lastName)
txtLastname.grid(row=4, column=1, pady=3, padx=40)
        
#Adress 
lblAddress = Label(LeftFrame, font=('arial', 14, 'bold'), text="Address:", padx=1)
lblAddress.grid(row=6, column=0, sticky=W)
txtAddress = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=address)
txtAddress.grid(row=6, column=1, pady=3, padx=40)
        
#Date of Birth
lblDOB = Label(LeftFrame, font=('arial', 14, 'bold'), text="Date Of Birth:", padx=1)
lblDOB.grid(row=8, column=0, sticky=W)
txtDOB = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dob)
txtDOB.grid(row=8, column=1, pady=3, padx=40)
        
#Mobile
lblMobile = Label(LeftFrame, font=('arial', 14, 'bold'), text="Mobile:", padx=1)
lblMobile.grid(row=10, column=0, sticky=W)
txtMobile = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=mobile)
txtMobile.grid(row=10, column=1, pady=3, padx=40)
        
#Email
lblEmail = Label(LeftFrame, font=('arial', 14, 'bold'), text="Email:", padx=1)
lblEmail.grid(row=12, column=0, sticky=W)
txtEmail = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=email)
txtEmail.grid(row=12, column=1, pady=3, padx=40)
        
#National
lblNational = Label(LeftFrame, font=('arial', 14, 'bold'), text="National:", padx=1)
lblNational.grid(row=14, column=0, sticky=W)
txtNational = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=national)
txtNational.grid(row=14, column=1, pady=3, padx=40)
        
#Gender 
lblGender = Label(LeftFrame, font=('arial', 14, 'bold'), text="Gender:", padx=1)
lblGender.grid(row=16, column=0, sticky=W)
# txtGender = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=gender)
txtGender = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=gender)
txtGender ['value'] = (' ', 'Male', 'Female', 'Other')
txtGender.current(0)
txtGender.grid(row=16, column=1, pady=3, padx=40)
        
#Date In
lblDateIn = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateIn:", padx=1)
lblDateIn.grid(row=18, column=0, sticky=W)
txtDateIn = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dateIn)
txtDateIn.grid(row=18, column=1, pady=3, padx=40)
        
#Date Out
lblDateOut = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateOut:", padx=1)
lblDateOut.grid(row=20, column=0, sticky=W)
txtDateOut = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dateOut)
txtDateOut.grid(row=20, column=1, pady=3, padx=40)
        
#proveID
lblProveID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of ID: ", padx=1, pady=2)
lblProveID.grid(row=22, column=0, sticky=W)
cboProveID = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=typeOfId)
cboProveID ['value'] = (' ', 'ID card', 'Passport')
cboProveID.current(0)
cboProveID.grid(row=22, column=1, pady=3, padx=2)
        
#type room 
lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of Room: ", padx=1, pady=2)
lblRoomType.grid(row=24, column=0, sticky=W)
cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=typeOfRoom)
cboRoomType ['value'] = (' ', 'Single', 'Double', 'Family')
cboRoomType.current(0)
cboRoomType.grid(row=24, column=1, pady=3, padx=2)
        
#order number room
lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Room Order: ", padx=1, pady=2)
lblRoomType.grid(row=26, column=0, sticky=W)
cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=roomOrder)
cboRoomType ['value'] = (' ', '001', '002', '003', '004', '005', '006', '007')
cboRoomType.current(0)
cboRoomType.grid(row=26, column=1, pady=3, padx=2)
cboRoomType.bind("<<ComboboxSelected>>")
        
#number floor
lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Number Floor: ", padx=1, pady=2)
lblNFloor.grid(row=28, column=0, sticky=W)
cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=numberFloor)
cboNFloor ['value'] = (' ', '1', '2', '3', '4', '5')
cboNFloor.current(0)
cboNFloor.grid(row=28, column=1, pady=3, padx=2)
cboNFloor.bind("<<ComboboxSelected>>")
#services
lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Services: ", padx=1, pady=2)
lblNFloor.grid(row=30, column=0, sticky=W)
cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=service)
cboNFloor ['value'] = (' ', 'Yes', 'No')
cboNFloor.current(0)
cboNFloor.grid(row=30, column=1, pady=3, padx=2)


        

        
#====================================================widgets================================================
        
scrollbar = Scrollbar(RightFrame2, orient=VERTICAL) #vertical cuộn theo hướng dọc 
manageHotel = ttk.Treeview(RightFrame2, height=22, columns=("cusID", "firstName", "lastName", "address", "dob", "mobile", "national", "gender", "dateIn", "dateOut","roomN", "totalCost"), yscrollcommand=scrollbar.set)
        
scrollbar.pack(side = RIGHT, fill=Y)
manageHotel.heading("cusID", text = "CusID")
manageHotel.heading("firstName", text = "First Name")
manageHotel.heading("lastName", text = "Last Name")
manageHotel.heading("address", text = "Address")
manageHotel.heading("dob", text = "Date Of Birth")
manageHotel.heading("mobile", text = "Mobile")
# manageHotel.heading("email", text = "Email") 
manageHotel.heading("national", text = "National")
manageHotel.heading("gender", text = "Gender")
manageHotel.heading("dateIn", text = "DateIn")
manageHotel.heading("dateOut", text = "DateOut")
manageHotel.heading("roomN", text = "RoomN")
manageHotel.heading("totalCost", text = "TotalCost")
        
manageHotel['show'] = 'headings'
        
manageHotel.column("cusID", width=60)
manageHotel.column("firstName", width=70)
manageHotel.column("lastName", width=70)
manageHotel.column("address", width=160)
manageHotel.column("dob", width=100)
manageHotel.column("mobile", width=80)
manageHotel.column("national", width=70)
manageHotel.column("gender", width=60)
manageHotel.column("dateIn", width=100)
manageHotel.column("dateOut", width=100)
manageHotel.column("roomN", width=60)
manageHotel.column("totalCost", width=60)
        
manageHotel.pack(fill= BOTH, expand=1)
manageHotel.bind("<ButtonRelease-1>", on_treeview_select)
# displayData()
#====================================================widgets================================================
# RoomNumber
        
# Room Number
lblDays = Label(RightFrame3, font=('arial', 14, 'bold'), text="Room Number: ",bd=5)
lblDays.grid(row=0, column=0, sticky=W) # W căn lb về lề bên trái
txtDays = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=roomN)
txtDays.grid(row = 0, column = 1)
        
# Number of days
lblDays = Label(RightFrame3, font=('arial', 14, 'bold'), text="No of Days: ",bd=5)
lblDays.grid(row=1, column=0, sticky=W) # W căn lb về lề bên trái
txtDays = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=totalDays)
txtDays.grid(row = 1, column = 1)
        
# Paid tax
lblPaidTax = Label(RightFrame3, font=('arial', 14, 'bold'), text="Paid Tax: ",bd=5)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=paidTax) # justify: căn chỉnh nội dung bên trong entry về bên trái
txtPaidTax.grid(row =2, column = 1)
        
#Sub Total
lblSubTotal = Label(RightFrame3, font=('arial', 14, 'bold'), text="Sub total: ",bd=5)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=subTotal) # justify: căchỉnh nội dung bên trong entry về bên trái
txtSubTotal.grid(row =3, column = 1)
        
#Total Cost
lblTotalCost = Label(RightFrame3, font=('arial', 14, 'bold'), text="Total cost: ",bd=5)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=totalCost) # justify: căchỉnh nội dung bên trong entry về bên trái
txtTotalCost.grid(row =4, column = 1)
        
        
 #====================================================Widgets Button================================================
#Add new and total
btnTotalandAddData = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="AddNewAndTotal", cursor='hand2', bg='#57a1f8', fg='white', command=totalCostAndAddData)
btnTotalandAddData.grid(row=0, column=0, padx=4, pady=1)
        
#Display
btnDisplay = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Display",cursor='hand2', bg='#57a1f8', fg='white', command=displayData).grid(row=0, column=1, padx=4, pady=1)
        
#Update
btnUpdate = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Update",cursor='hand2', bg='#57a1f8', fg='white', command=update).grid(row=0,column=2, padx=4, pady=1)
        
#Search
btnSearch = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Search",cursor='hand2', bg='#57a1f8', fg='white', command=search).grid(row=0,column=4, padx=4, pady=1)
        
#Delete
btnDelete = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Delete",cursor='hand2', bg='#57a1f8', fg='white', command=delete).grid(row=0,column=3, padx=4, pady=1)
        
#Reset
btnReset = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Reset",cursor='hand2', bg='#57a1f8', fg='white', command=Reset).grid(row=0,column=5, padx=4, pady=1)
        
# Exit
btnExit = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=14, height=2, text="Exit",cursor='hand2', bg='#57a1f8', fg='white', command=iExit).grid(row=0,column=6, padx=4, pady=1)
        
hotel.mainloop()