from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
# connect MySQL
import pymysql
import mysql.connector
import datetime
import time
from datetime import datetime, timedelta

#FRONTEND
class Hotel: 
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Database Management system")
        self.root.geometry("1600x800+0+0") #thay đổi kích thước của cửa sổ +0+0 tương ứng với đặt nó vào vị trí góc trên trái của màn hình
        
        #Main
        MainFrame = Frame(self.root)
        MainFrame.grid() #grid tạo lưới 
        
        #Top
        TopFrame = Frame(MainFrame, bd=10, width=1600, height=650, padx=2, relief=RIDGE) #relief kiểu cài đặt viền
        TopFrame.pack(side=TOP)
        
        #Left
        LeftFrame = Frame(TopFrame, bd=5, width=400, height=650, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        #Right
        RightFrame = Frame(TopFrame, bd=5, width=1080, height=650, relief=RIDGE)
        RightFrame.pack(side=RIGHT)
        
        # RightFrame1 = Frame(RightFrame, bd = 5, width=1050, height=50, padx=10, relief=RIDGE)
        # RightFrame1.grid(row=0, column=0)
        RightFrame2 = Frame(RightFrame, bd = 5, width=1050, height=200, padx=3, relief=RIDGE)
        RightFrame2.grid(row=0, column=0)
        RightFrame3 = Frame(RightFrame, bd = 5, width=1050, height=300, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3, column=0)
        
        #Bottom
        BottonFrame = Frame(MainFrame, bd = 10, width=1530, height=150, padx=2, relief=RIDGE)
        BottonFrame.pack(side=BOTTOM)
        
        #===========================Variable desc====================
        global hd
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
        # roomN.set(roomOrder.get() + numberFloor.get())

        
        
        
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
                root.destroy()
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

            
            # self.txtCusID.delete(0, END)
            self.txtFristname.delete(0, END)
            self.txtLastname.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtNational.delete(0, END)
            self.txtGender.delete(0, END)
            
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
            
        
        # totalCostAndAdData:
        def totalCostAndAddData():
            valueTotalCost()
            roomNumber()
            if (mobile.get() == "" or service.get() == "" or typeOfRoom.get() == "" or numberFloor.get() == "" or roomOrder.get() == ""):
                tkinter.messagebox.showerror("Provide number phone,  and service")
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
                cur.execute("select cusID, firstName, lastName, address, dob, mobile, national, gender, dateIn, dateOut, roomN, totalCost from hotel_management.hotel2")
                result = cur.fetchall() # lấy hết kết quả hàng từ truy vấn
                if len(result) != 0:
                    # xóa tất cả các hàng hiện có trong treeview
                    self.manageHotel.delete(*self.manageHotel.get_children())
                    
                    # chèn lại tất cả dữ liệu đã truy vấn vào trên treeview
                    for row in result:
                        self.manageHotel.insert('',END, values=row)
                sqlCon.commit()
            except mysql.connector.Error as err:
                tk.messagebox.showerror("Database Error", f"An error occurred: {err}")
            finally:
                if sqlCon.is_connected():
                    cur.close()
                    sqlCon.close()
        
        # click one Data 
        def on_treeview_select(event):
            selected_item = self.manageHotel.selection()[0]
            cus_id = self.manageHotel.item(selected_item, 'values')[0]
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
        
        #search
        def search():
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
                    tkinter.messagebox.showinfo("Form nhập liệu", "không tìm thấy bản ghi nào")
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
        
        #===========================Widget=================
        # #tạo mã định doanh khách hàng
        self.lblCusID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Customer Ref:", padx=1)
        self.lblCusID.grid(row=0, column=0, sticky=W)
        self.txtCusID = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=cusID)
        self.txtCusID.grid(row=0, column=1, pady=3, padx=40)
        
        #Firstname
        self.lblFristname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Frist Name:", padx=1)
        self.lblFristname.grid(row=2, column=0, sticky=W)
        self.txtFristname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=firstName)
        self.txtFristname.grid(row=2, column=1, pady=3, padx=40)
        
        #Lastname
        self.lblLastname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Last Name:", padx=1)
        self.lblLastname.grid(row=4, column=0, sticky=W)
        self.txtLastname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=lastName)
        self.txtLastname.grid(row=4, column=1, pady=3, padx=40)
        
        #Adress 
        self.lblAddress = Label(LeftFrame, font=('arial', 14, 'bold'), text="Address:", padx=1)
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=address)
        self.txtAddress.grid(row=6, column=1, pady=3, padx=40)
        
        #Date of Birth
        self.lblDOB = Label(LeftFrame, font=('arial', 14, 'bold'), text="Date Of Birth:", padx=1)
        self.lblDOB.grid(row=8, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dob)
        self.txtDOB.grid(row=8, column=1, pady=3, padx=40)
        
        #Mobile
        self.lblMobile = Label(LeftFrame, font=('arial', 14, 'bold'), text="Mobile:", padx=1)
        self.lblMobile.grid(row=10, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=mobile)
        self.txtMobile.grid(row=10, column=1, pady=3, padx=40)
        
        #Email
        self.lblEmail = Label(LeftFrame, font=('arial', 14, 'bold'), text="Email:", padx=1)
        self.lblEmail.grid(row=12, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=email)
        self.txtEmail.grid(row=12, column=1, pady=3, padx=40)
        
        #National
        self.lblNational = Label(LeftFrame, font=('arial', 14, 'bold'), text="National:", padx=1)
        self.lblNational.grid(row=14, column=0, sticky=W)
        self.txtNational = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=national)
        self.txtNational.grid(row=14, column=1, pady=3, padx=40)
        
        #Gender 
        self.lblGender = Label(LeftFrame, font=('arial', 14, 'bold'), text="Gender:", padx=1)
        self.lblGender.grid(row=16, column=0, sticky=W)
        # self.txtGender = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=gender)
        self.txtGender = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=gender)
        self.txtGender ['value'] = (' ', 'Male', 'Female', 'Other')
        self.txtGender.current(0)
        self.txtGender.grid(row=16, column=1, pady=3, padx=40)
        
        #Date In
        self.lblDateIn = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateIn:", padx=1)
        self.lblDateIn.grid(row=18, column=0, sticky=W)
        self.txtDateIn = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dateIn)
        self.txtDateIn.grid(row=18, column=1, pady=3, padx=40)
        
        #Date Out
        self.lblDateOut = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateOut:", padx=1)
        self.lblDateOut.grid(row=20, column=0, sticky=W)
        self.txtDateOut = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18, textvariable=dateOut)
        self.txtDateOut.grid(row=20, column=1, pady=3, padx=40)
        
        #proveID
        self.lblProveID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of ID: ", padx=1, pady=2)
        self.lblProveID.grid(row=22, column=0, sticky=W)
        self.cboProveID = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=typeOfId)
        self.cboProveID ['value'] = (' ', 'ID card', 'Passport')
        self.cboProveID.current(0)
        self.cboProveID.grid(row=22, column=1, pady=3, padx=2)
        
        #type room 
        self.lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of Room: ", padx=1, pady=2)
        self.lblRoomType.grid(row=24, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=typeOfRoom)
        self.cboRoomType ['value'] = (' ', 'Single', 'Double', 'Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=24, column=1, pady=3, padx=2)
        
        #order number room
        self.lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Room Order: ", padx=1, pady=2)
        self.lblRoomType.grid(row=26, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=roomOrder)
        self.cboRoomType ['value'] = (' ', '001', '002', '003', '004', '005', '006', '007')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=26, column=1, pady=3, padx=2)
        self.cboRoomType.bind("<<ComboboxSelected>>")
        
        #number floor
        self.lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Number Floor: ", padx=1, pady=2)
        self.lblNFloor.grid(row=28, column=0, sticky=W)
        self.cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=numberFloor)
        self.cboNFloor ['value'] = (' ', '1', '2', '3', '4', '5')
        self.cboNFloor.current(0)
        self.cboNFloor.grid(row=28, column=1, pady=3, padx=2)
        self.cboNFloor.bind("<<ComboboxSelected>>")
        #services
        self.lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Services: ", padx=1, pady=2)
        self.lblNFloor.grid(row=30, column=0, sticky=W)
        self.cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17, textvariable=service)
        self.cboNFloor ['value'] = (' ', 'Yes', 'No')
        self.cboNFloor.current(0)
        self.cboNFloor.grid(row=30, column=1, pady=3, padx=2)
        

        
        #====================================================widgets================================================
        
        scrollbar = Scrollbar(RightFrame2, orient=VERTICAL) #vertical cuộn theo hướng dọc 
        self.manageHotel = ttk.Treeview(RightFrame2, height=22, columns=("cusID", "firstName", "lastName", "address", "dob", "mobile", "national", "gender", "dateIn", "dateOut","roomN", "totalCost"), yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side = RIGHT, fill=Y)
        self.manageHotel.heading("cusID", text = "CusID")
        self.manageHotel.heading("firstName", text = "First Name")
        self.manageHotel.heading("lastName", text = "Last Name")
        self.manageHotel.heading("address", text = "Address")
        self.manageHotel.heading("dob", text = "Date Of Birth")
        self.manageHotel.heading("mobile", text = "Mobile")
        # self.manageHotel.heading("email", text = "Email") 
        self.manageHotel.heading("national", text = "National")
        self.manageHotel.heading("gender", text = "Gender")
        self.manageHotel.heading("dateIn", text = "DateIn")
        self.manageHotel.heading("dateOut", text = "DateOut")
        self.manageHotel.heading("roomN", text = "RoomN")
        self.manageHotel.heading("totalCost", text = "TotalCost")
        
        self.manageHotel['show'] = 'headings'
        
        self.manageHotel.column("cusID", width=60)
        self.manageHotel.column("firstName", width=70)
        self.manageHotel.column("lastName", width=70)
        self.manageHotel.column("address", width=160)
        self.manageHotel.column("dob", width=100)
        self.manageHotel.column("mobile", width=80)
        self.manageHotel.column("national", width=70)
        self.manageHotel.column("gender", width=60)
        self.manageHotel.column("dateIn", width=100)
        self.manageHotel.column("dateOut", width=100)
        self.manageHotel.column("roomN", width=60)
        self.manageHotel.column("totalCost", width=60)
        
        self.manageHotel.pack(fill= BOTH, expand=1)
        self.manageHotel.bind("<ButtonRelease-1>", on_treeview_select)
        # displayData()
        #====================================================widgets================================================
        # RoomNumber
        
        # Room Number
        self.lblDays = Label(RightFrame3, font=('arial', 14, 'bold'), text="Room Number: ",bd=5)
        self.lblDays.grid(row=0, column=0, sticky=W) # W căn lb về lề bên trái
        self.txtDays = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=roomN)
        self.txtDays.grid(row = 0, column = 1)
        
        # Number of days
        self.lblDays = Label(RightFrame3, font=('arial', 14, 'bold'), text="No of Days: ",bd=5)
        self.lblDays.grid(row=1, column=0, sticky=W) # W căn lb về lề bên trái
        self.txtDays = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=totalDays)
        self.txtDays.grid(row = 1, column = 1)
        
        # Paid tax
        self.lblPaidTax = Label(RightFrame3, font=('arial', 14, 'bold'), text="Paid Tax: ",bd=5)
        self.lblPaidTax.grid(row=2, column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=paidTax) # justify: căn chỉnh nội dung bên trong entry về bên trái
        self.txtPaidTax.grid(row =2, column = 1)
        
        #Sub Total
        self.lblSubTotal = Label(RightFrame3, font=('arial', 14, 'bold'), text="Sub total: ",bd=5)
        self.lblSubTotal.grid(row=3, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=subTotal) # justify: căn chỉnh nội dung bên trong entry về bên trái
        self.txtSubTotal.grid(row =3, column = 1)
        
        #Total Cost
        self.lblTotalCost = Label(RightFrame3, font=('arial', 14, 'bold'), text="Total cost: ",bd=5)
        self.lblTotalCost.grid(row=4, column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3, font=('arial', 14, 'bold'), width= 80, justify=LEFT, textvariable=totalCost) # justify: căn chỉnh nội dung bên trong entry về bên trái
        self.txtTotalCost.grid(row =4, column = 1)
        
        
         #====================================================Widgets Button================================================
        #Add new and total
        self.btnTotalandAddData = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="AddNew/Total", command=totalCostAndAddData).grid(row=0, column=0, padx=4, pady=1)
        
        #Display
        self.btnDisplay = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Display", command=displayData).grid(row=0, column=1, padx=4, pady=1)
        
        #Update
        self.btnUpdate = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Update", command=update).grid(row=0, column=2, padx=4, pady=1)
        
        #Search
        self.btnSearch = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Search", command=search).grid(row=0, column=4, padx=4, pady=1)
        
        #Delete
        self.btnDelete = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Delete", command=delete).grid(row=0, column=3, padx=4, pady=1)
        
        #Reset
        self.btnReset = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=15, height=2, text="Reset", command=Reset).grid(row=0, column=5, padx=4, pady=1)
        
        # Exit
        self.btnExit = Button(BottonFrame, bd=4, font=('arial', 16, 'bold'), width=14, height=2, text="Exit", command=iExit).grid(row=0, column=6, padx=4, pady=1)
        
if __name__ == '__main__':
    root = Tk()
    application = Hotel (root) 
    root.mainloop()