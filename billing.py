from tkinter import*
from tkinter import ttk,messagebox
import os
##from PILLOW import Image,ImageTk 
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Manangement System | Developed by Khushi")
        self.root.config(bg="#eee2dc")

        self.icon_title = PhotoImage(file="")  ####image1
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#edc7b7",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)


        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("Times New Roman",15,"bold"),bg="lavender",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===CLOCK===#
        self.lbl_clock=Label(self.root,text="Welcome to Utkal Alumina Inventory Manangement System\t\tDate:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("times new roman",15),bg="#eee2dc",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30) 


        #####product frame

        self.var_search=StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="ALL Products",font=("goudy old style",20,"bold"),bg="#ac3b61",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="lavender")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="lavender",fg="black").place(x=2,y=5)
        

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="lavender",fg="black").place(x=2,y=45)

        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow",fg="black").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style ",15),cursor="hand2",bg="#ac3b61",fg="white").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style ",15),cursor="hand2",bg="#ac3b61",fg="white").place(x=285,y=10,width=100,height=25)



        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)

        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3, orient=VERTICAL)

        scrollx=Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name", "specification", "qty","status","timeline"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("specification", text="Specification")
        self.product_Table.heading("qty", text="Qty")
        self.product_Table.heading("status", text="Status")
        self.product_Table.heading("timeline", text="Timeline")
        

        self.product_Table["show"]="headings"


        self.product_Table.column("pid",width=90)
        self.product_Table.column("name", width=100)
        self.product_Table.column("specification",width=100)
        self.product_Table.column("qty", width=100)
        self.product_Table.column("status", width=100)
        self.product_Table.column("timeline", width=100)
        



 

        self.product_Table.pack(fill=BOTH,expand=1)
       #self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="lavender",fg="black").pack(side=BOTTOM,fill=X)
        
        ###############################employee FRAME
        #self.show()
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        EmployeeFrame=Frame(self.root,bd=4,bg="lavender",relief=RIDGE)
        EmployeeFrame.place(x=420,y=110,width=530,height=70)

        eTitle=Label(EmployeeFrame,text="Employee Details",font=("goudy old style",15),bg="#ac3b61",fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(EmployeeFrame,text="Name",font=("times new roman",15),bg="lavender",fg="black").place(x=5,y=35)

        txt_name=Entry(EmployeeFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow",fg="black").place(x=80,y=35,width=180)
        lbl_contact=Label(EmployeeFrame,text="Contact No.",font=("times new roman",15),bg="lavender",fg="black").place(x=270,y=35)

        txt_contact=Entry(EmployeeFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow",fg="black").place(x=380,y=35,width=140)
        
        Cal_Cart_Frame=Frame(self.root,bd=2,bg="lavender",relief=RIDGE)
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

#####cal frame
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,bg="white",relief=RIDGE)
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text=7,font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text=8,font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text=9,font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text=4,font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text=5,font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text=6,font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text=1,font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text=2,font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text=3,font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text=0,font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,bg="#edc7b7",width=4,pady=11.5,cursor="hand2").grid(row=4,column=3)


        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)

        cart_Frame.place(x=280,y=8,width=245,height=342)

        cartTitle=Label(cart_Frame,text="Cart \t Total Products: [0]",font=("goudy old style",15),bg="#ac3b61",fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame, orient=VERTICAL)

        scrollx=Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","specification", "qty","status","timeline"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="PID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("specification", text="Specification")
        self.CartTable.heading("qty", text="Qty")
        self.CartTable.heading("status", text="Status")
        self.CartTable.heading("timeline", text="Timeline")
        

        self.CartTable["show"]="headings"


        self.CartTable.column("pid",width=40)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=90)
        self.CartTable.column("specification",width=130)
        self.CartTable.column("qty", width=30)
        self.CartTable.column("status", width=90)
        self.CartTable.column("timeline", width=90)
        



 

        self.CartTable.pack(fill=BOTH,expand=1)
       #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
####add cart buttons

        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_specification=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_timeline=StringVar()
        
        
        

        Add_CartWidgetsFrame=Frame(self.root,bd=2,bg="lavender",relief=RIDGE)
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="lavender").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        lbl_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="lavender").place(x=230,y=5)
        txt_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_qty=Label(Add_CartWidgetsFrame,text="Qty",font=("times new roman",15),bg="lavender").place(x=390,y=5)
        txt_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock [1000]",font=("times new roman",15),bg="lavender")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="#ac3b61",fg="white",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add=Button(Add_CartWidgetsFrame,text="Add | Update cart",font=("times new roman",15,"bold"),bg="#ac3b61",fg="white",cursor="hand2").place(x=340,y=70,width=180,height=30)


        ################all functions

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)   


    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))   


    def logout(self):
        self.root.destroy()
        os.system("python login.py")      
           

if __name__=="__main__":
    root=Tk()
    obj= BillClass(root)
    root.mainloop()        