from tkinter import*
##from PILl import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
#import Calendar 



class productClass:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Manangement System | Developed by Khushi")
        self.root.config(bg="lightpink")
        self.root.focus_force()


        #################################



        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[] 
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_specification=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_timeline=StringVar()   

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="lightpink")
        product_Frame.place(x=10,y=10,width=450,height=480)


        title=Label(product_Frame,text=" Manage Product Details",font=("goudy old style",18),bg="#ac3b61",fg="black",cursor="hand2").pack(side=TOP,fill=X)
####col1
        lbl_category=Label(self.root,text="Category",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="Supplier",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=100)
        lbl_product_name=Label(self.root,text="Name",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=140)
        lbl_specification=Label(self.root,text="Specification",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=180)
        lbl_qty=Label(self.root,text="Quantity",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=220)
        lbl_status=Label(self.root,text="Status",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=260)
        lbl_timeline=Label(self.root,text="Timeline",font=("goudy old style",15),bg="lightpink",fg="black",cursor="hand2").place(x=30,y=300)




      ####ocol2


        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=45,width=200) 
        cmb_cat.current(0)


        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=90,width=200) 
        cmb_sup.current(0) 


        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=130,width=200)

        txt_specification=Entry(product_Frame,textvariable=self.var_specification,font=("goudy old style",15),bg="lightyellow").place(x=150,y=170,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)

       
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=247,width=200) 
        cmb_status.current(0) 


        cmb_timeline=ttk.Combobox(product_Frame,textvariable=self.var_timeline,values=("Select","Permanent","Temporary(until work is done)"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_timeline.place(x=150,y=290,width=200) 
        cmb_timeline.current(0)


        


        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#ac3b61",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)

        btn_update=Button(product_Frame,text="Update", command=self.update,font=("goudy old style",15),bg="#ac3b61",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete", command=self.delete,font=("goudy old style",15),bg="#ac3b61",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#ac3b61",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40) 


        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE, bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
          
######options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180) 
        cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#ac3b61",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

        ####pdetail

        p_frame=Frame(self.root,bd=3,relief=RIDGE)

        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame, orient=VERTICAL)

        scrollx=Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","Category", "Supplier", "name", "specification", "qty", "status", "Timeline"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("specification", text="Specification")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")
        self.product_table.heading("Timeline", text="Timeline")
       

        self.product_table["show"]="headings"


        self. product_table.column("pid",width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("specification", width=100)
        self.product_table.column("qty", width=100)
        self. product_table.column("status", width=100)
        self. product_table.column("Timeline", width=100)
        



 

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)


        self.show()
        




    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category ")
            cat=cur.fetchall()
            self.cat_list.append("Empty")

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
            
                for i in cat:
                  self.cat_list.append(i[0])
               

            cur.execute("Select name from supplier")
            sup=cur.fetchall()

            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
            
                for i in sup:
                  self.sup_list.append(i[0])
            

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    
            

    def add(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="": ##or self.var_name.get()==""
                messagebox.showerror("Error","All fields are required required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None: 
                    messagebox.showerror("Error","Product already available,try different",parent=self.root)   
                else:
                    cur.execute("INSERT INTO product (Category, Supplier, name, specification, qty, status, Timeline) values (?, ?, ?, ?, ?, ?, ?)" , ( 
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_specification.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),

                                        self.var_timeline.get(),

                                        
                                        

        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def show(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

            
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_specification.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),

        self.var_timeline.set(row[7]),
    
                    


    def update(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="": ##or self.var_name.get()==""
                messagebox.showerror("Error","Please select product from list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None: 
                    messagebox.showerror("Error","Invalid Product",parent=self.root)   
                else:
                    cur.execute("UPDATE product set Category=?, Supplier=?, name=?, specification=?, qty=?, status=?, timeline=? where pid=?", ( 
                                        
                                      self.var_cat.get(),
                                      self.var_sup.get(),
                                      self.var_name.get(),
                                      self.var_specification.get(),
                                      self.var_qty.get(),
                                      self.var_status.get(),
                                      self.var_timeline.get(),
                                      self.var_pid.get()
                                        

        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)

                    self.show()
                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="": ##or self.var_name.get()==""
                messagebox.showerror("Error","Select product from list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None: 
                    messagebox.showerror("Error","Invalid Product",parent=self.root)   
                else:
                    op=messagebox.askyesno("Confirm","Do you Really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

        
    def clear(self):
        
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_specification.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_timeline.set(""),
        self.var_pid.set("")
        
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
                    
    def search(self):
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
                
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")    

                rows=cur.fetchall()
                if len(rows)!=0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else: 
                    messagebox.showerror("Error","No record found!!!",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)     


        
if __name__=="__main__":

    root=Tk()           
    obj= productClass(root)
    root.mainloop()                