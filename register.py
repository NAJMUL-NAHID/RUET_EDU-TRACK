from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("RUET EduTrack")
        self.root.geometry("1350x700+50+30")
        self.root.config(bg="white")
        left_lbl=Label(self.root,bg="#031F3C",bd=0)
        left_lbl.place(x=0,y=0,width=600,relheight=1)

        right_lbl=Label(self.root,bg="#08A3D2",bd=0)
        right_lbl.place(x=600,y=0,relwidth=1,relheight=1)

        #=====register=====frame=====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=180,y=100,width=1000,height=500)
        

        self.ruet_logo=Image.open("images/logo_ruet.png")
        self.ruet_logo=self.ruet_logo.resize((300,360),Image.Resampling.LANCZOS)
        self.ruet_logo=ImageTk.PhotoImage(self.ruet_logo)
        self.ruet_logo_lbl=Label(frame1,image=self.ruet_logo,bg="#FFFFFF",bd=0).place(x=20,y=50,width=300,height=360)





        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=350,y=30)
        #=====label=====and=====entry=====
        #name===row===1=====
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=350,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=670,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=670,y=130,width=250)
        
        #contact=====and======email======row===2=====
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=350,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=670,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=670,y=200,width=250)

        #====row===3
        question=Label(frame1,text="Security Question ",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=240)
           
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your Birth Place","Your Pet Name","Your Best Friend Name")
        self.cmb_quest.place(x=350,y=270,height=27,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=670,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=670,y=270,width=250)
        #====row===4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=350,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=670,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=670,y=340,width=250)
        #====terms===and===condition===row===5
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree To The Terms And Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white",fg="green",activebackground="white",activeforeground="black").place(x=350,y=380)


        #====register===button===row===6
        btn_register=Button(frame1,text="Register",font=("times new roman",15,"bold"),bg="#0813D2",fg="white",bd=0,cursor="hand2",command=self.register_data).place(x=350,y=420,width=150,height=40)
        btn_login=Button(frame1,text="Login",font=("times new roman",15,"bold"),bg="green",fg="white",bd=0,cursor="hand2",command=self.login_window).place(x=520,y=420,width=150,height=40)


    #=======functions====

    def login_window(self):
      self.root.destroy()
      os.system("python login.py")       


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.var_chk.set(0)   

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password And Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree To The Terms And Conditions",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User Already Exist, Please Try Another Email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_quest.get(),
                        self.txt_answer.get(),
                        self.txt_password.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To {str(es)}",parent=self.root)
            
    
          
        

    

root=Tk()
obj=Register(root)
root.mainloop()
      