from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
# connect MySQL

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
        
        RightFrame1 = Frame(RightFrame, bd = 5, width=1050, height=50, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)
        RightFrame2 = Frame(RightFrame, bd = 5, width=1050, height=150, padx=3, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)
        RightFrame3 = Frame(RightFrame, bd = 5, width=1050, height=450, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3, column=0)
        
        #Bottom
        BottomFrame = Frame(MainFrame, bd = 10, width=1530, height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)
        
        #===========================Widget=================
        # #tạo mã định doanh khách hàng
        self.lblCusID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Customer Ref:", padx=1)
        self.lblCusID.grid(row=0, column=0, sticky=W)
        self.txtCusID = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtCusID.grid(row=0, column=1, pady=3, padx=40)
        
        #Firstname
        self.lblFristname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Frist Name:", padx=1)
        self.lblFristname.grid(row=2, column=0, sticky=W)
        self.txtFristname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtFristname.grid(row=2, column=1, pady=3, padx=40)
        
        #Lastname
        self.lblLastname = Label(LeftFrame, font=('arial', 14, 'bold'), text="Last Name:", padx=1)
        self.lblLastname.grid(row=4, column=0, sticky=W)
        self.txtLastname = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtLastname.grid(row=4, column=1, pady=3, padx=40)
        
        #Adress 
        self.lblAddress = Label(LeftFrame, font=('arial', 14, 'bold'), text="Address:", padx=1)
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtAddress.grid(row=6, column=1, pady=3, padx=40)
        
        #Date of Birth
        self.lblDOB = Label(LeftFrame, font=('arial', 14, 'bold'), text="Date Of Birth:", padx=1)
        self.lblDOB.grid(row=8, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtDOB.grid(row=8, column=1, pady=3, padx=40)
        
        #Mobile
        self.lblMobile = Label(LeftFrame, font=('arial', 14, 'bold'), text="Mobile:", padx=1)
        self.lblMobile.grid(row=10, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtMobile.grid(row=10, column=1, pady=3, padx=40)
        
        #Email
        self.lblEmail = Label(LeftFrame, font=('arial', 14, 'bold'), text="Email:", padx=1)
        self.lblEmail.grid(row=12, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtEmail.grid(row=12, column=1, pady=3, padx=40)
        
        #National
        self.lblNational = Label(LeftFrame, font=('arial', 14, 'bold'), text="National:", padx=1)
        self.lblNational.grid(row=14, column=0, sticky=W)
        self.txtNational = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtNational.grid(row=14, column=1, pady=3, padx=40)
        
        #Gender 
        self.lblGender = Label(LeftFrame, font=('arial', 14, 'bold'), text="Gender:", padx=1)
        self.lblGender.grid(row=16, column=0, sticky=W)
        self.txtGender = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtGender.grid(row=16, column=1, pady=3, padx=40)
        
        #Date In
        self.lblDateIn = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateIn:", padx=1)
        self.lblDateIn.grid(row=18, column=0, sticky=W)
        self.txtDateIn = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtDateIn.grid(row=18, column=1, pady=3, padx=40)
        
        #Date Out
        self.lblDateOut = Label(LeftFrame, font=('arial', 14, 'bold'), text="DateOut:", padx=1)
        self.lblDateOut.grid(row=20, column=0, sticky=W)
        self.txtDateOut = Entry(LeftFrame, font=('arial', 14, 'bold'), width=18)
        self.txtDateOut.grid(row=20, column=1, pady=3, padx=40)
        
        #proveID
        self.lblProveID = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of ID: ", padx=1, pady=2)
        self.lblProveID.grid(row=22, column=0, sticky=W)
        self.cboProveID = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17)
        self.cboProveID ['value'] = (' ', 'ID card', 'Passport')
        self.cboProveID.current(0)
        self.cboProveID.grid(row=22, column=1, pady=3, padx=2)
        
        #type room 
        self.lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Type Of Room: ", padx=1, pady=2)
        self.lblRoomType.grid(row=24, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17)
        self.cboRoomType ['value'] = (' ', 'Single', 'Double', 'Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=24, column=1, pady=3, padx=2)
        
        #number room
        self.lblRoomType = Label(LeftFrame, font=('arial', 14, 'bold'), text="Room No: ", padx=1, pady=2)
        self.lblRoomType.grid(row=26, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17)
        self.cboRoomType ['value'] = (' ', '001', '002', '003', '004', '005', '006', '007')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=26, column=1, pady=3, padx=2)
        
        #number floor
        self.lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Number Floor: ", padx=1, pady=2)
        self.lblNFloor.grid(row=28, column=0, sticky=W)
        self.cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17)
        self.cboNFloor ['value'] = (' ', '1', '2', '3', '4', '5')
        self.cboNFloor.current(0)
        self.cboNFloor.grid(row=28, column=1, pady=3, padx=2)
        
        #facilities
        self.lblNFloor = Label(LeftFrame, font=('arial', 14, 'bold'), text="Facilities: ", padx=1, pady=2)
        self.lblNFloor.grid(row=30, column=0, sticky=W)
        self.cboNFloor = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 14, 'bold'), width=17)
        self.cboNFloor ['value'] = (' ', 'Yes', 'No')
        self.cboNFloor.current(0)
        self.cboNFloor.grid(row=30, column=1, pady=3, padx=2)
if __name__ == '__main__':
    root = Tk()
    application = Hotel (root) 
    root.mainloop()