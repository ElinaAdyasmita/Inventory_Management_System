from tkinter import*
##from PILl import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
#import Calendar 
import os




class salesClass:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Manangement System | Developed by Khushi")
        self.root.config(bg="lightpink")
        self.root.focus_force()
        self.order_list=[]
        self.var_invoice=StringVar()


        #title
        lbl_title=Label(self.root,text="Manage Product Order ",font=("goudy old style",30),bg="#ac3b61",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="lightpink").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)

        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#ac3b61",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#ac3b61",fg="white",cursor="hand2").place(x=490,y=100,width=120,height=28)


        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_frame, orient=VERTICAL)

        #scrollx=Scrollbar(sales_frame, orient=HORIZONTAL)

        self.Sales_List=Listbox(sales_frame,font=("goudy old style",15),bg="lightpink",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)

####order area
        order_frame=Frame(self.root,bd=3,relief=RIDGE)
        order_frame.place(x=280,y=140,width=410,height=330)
        lbl_title2=Label(order_frame,text="Employee Order Area ",font=("goudy old style",15),bg="#ac3b61",fg="white").pack(side=TOP,fill=X)
        scrolly2=Scrollbar(order_frame, orient=VERTICAL)

        #scrollx=Scrollbar(sales_frame, orient=HORIZONTAL)

        self.order_area=Text(order_frame,font=("goudy old style",15),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.order_area.yview)
        self.order_area.pack(fill=BOTH,expand=1)


        self.show()


        ######################################################

    def show(self):
        del self.order_list[:]
        self.Sales_List.delete(0,END)
        for i in os.listdir('order'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.order_list.append(i.split('.')[0])

        #print(os.listdir('order'))
    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        
        #print(file_name)
        self.order_area.delete('1.0',END)
        fp=open(f'order/{file_name}','r')
        for i in fp:
            self.order_area.insert(END,i)

        fp.close()   

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.order_list:

                fp=open(f'order/{self.var_invoice.get()}.txt','r')
                self.order_area.delete('1.0',END)
                for i in fp:
                   
                   self.order_area.insert(END,i)

                fp.close()

            else:
                messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)    

    def clear(self):
        self.show()
        self.order_area.delete('1.0',END)                   


if __name__=="__main__":
    root=Tk()           
    obj= salesClass(root)
    root.mainloop()