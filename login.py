from tkinter import*
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed By Khushi ")
        self.root.geometry("1350x700+0+0")
          #===images===========

        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="lightpink")
        login_frame.place(x=460,y=90,width=450,height=470)
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="#eee2dc").place(x=0,y=30,relwidth=1) 

        
        lbl_user=Label(login_frame, text="Employee ID", font=("Andalus",15),bg="lightpink",fg="black").place(x=50,y=100)
        

        txt_employee_id=Entry(login_frame,textvariable=self.employee_id, font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=350,height=45)


                
        lbl_pass=Label(login_frame, text="Password", font=("Andalus",15),bg="lightpink",fg="black").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=350,height=45)


        

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold", 15), bg="#ac3b61",activebackground='#ac3b61',fg="white",activeforeground="white",cursor="hand2").place(x=100,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=100,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white", fg="lightgray",font=("times new roman",15,"bold")).place(x=200,y=355) 



        btn_forget=Button(login_frame, text="Forget Password?",command=self.forget_window,font=("times new roman",13),cursor="hand2",bg="lightpink",fg="darkblue",bd=0,activebackground="lightpink",activeforeground='#ac3b61').place(x=160,y=390)


       

       

        
    def login(self):

        
        con=sqlite3.connect(database=r'ims_db.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)

            else:

               cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
               user=cur.fetchone()
               if user==None:
                   messagebox.showerror('Error',"Invalid Username/Password",parent=self.root)

               else:
                   if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py") 

                   else: 
                       self.root.destroy()
                       os.system("python billing.py")      

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


                
    def forget_window(self):

        con = sqlite3.connect(database=r'ims_db.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror('Error', "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT email FROM employee WHERE eid=?", (self.employee_id.get(),)) 
                email = cur.fetchone()
                if email is None:
                    messagebox.showerror('Error', "Invalid Employee ID", parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    # call send_email_function()
                    self.forget_win = Toplevel(self.root)
                    self.forget_win.title('Reset Password')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()

                    title = Label(self.forget_win, text='Reset Password', font=('goudy old style', 15, 'bold'), bg="lightpink", fg="black").pack(side=TOP, fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter otp sent on registered email",font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='lightyellow').place(x=20,y=100,width=250,height=30)
                    self.btn_reset=Button(self.forget_win,text="Submit",font=("times new roman",15),cursor="hand2",bg='lightblue')
                    self.btn_reset.place(x=280,y=100,width=100,height=30)

                    lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)


                    lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)

                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED,font=("times new roman",15),cursor="hand2",bg='lightblue')
                    self.btn_update.place(x=150,y=300,width=100,height=30)


                    


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)




    
root=Tk()
obj=Login_System(root)
root.mainloop()