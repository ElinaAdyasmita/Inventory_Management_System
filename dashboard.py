from tkinter import*
##from PILLOW import Image,ImageTk 
from Employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
import os
from sales import salesClass



class IMS:
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
         
         #===left menu====#
        ##self.MenuLogo=Image.open("Image/menu_im.png") ####image2
        ##self.MenuLogo=self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        ##self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="lavender")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        ### >>>

        ##lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        ##lbl_menuLogo.pack(side=TOP,fill=X)

        ##self.icon_title=PhotoImage(file="image/")
        lbl_menu=Label(LeftMenu,text="Menu",font=("Times New Roman",20,""),bg="lavender").pack(side=TOP,fill=X)
        

        
        btn=Button(LeftMenu,text="Employee",command=self.employee,font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn=Button(LeftMenu,text="Supplier",command=self.supplier,font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn=Button(LeftMenu,text="Category",command=self.category,font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn=Button(LeftMenu,text="Products",command=self.product,font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn=Button(LeftMenu,text="Sales",command=self.sales,font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn=Button(LeftMenu,text="Exit",font=("Times New Roman",20,"bold"),bg="#ac3b61",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        self.lbl_employee=Label(self.root,text="Total Employee\n[0]", bd=5,relief=RIDGE,bg="#ac3b61",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]", bd=5,relief=RIDGE,bg="#ac3b61",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[0]", bd=5,relief=RIDGE,bg="#ac3b61",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]", bd=5,relief=RIDGE,bg="#ac3b61",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]", bd=5,relief=RIDGE,bg="#ac3b61",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        lbl_footer=Label(self.root,text="Inventory Manangement System/Developed by Khushi/nFor any technical issue:8319112808",font=("times new roman",12),bg="#865d36",fg="black").pack(side=BOTTOM,fill=X)

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)    


    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)    
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win) 

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj= IMS(root)
    root.mainloop()