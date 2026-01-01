from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import os
import smtplib
import random
os.system("python create_db.py")
class Login_window:
   def __init__(self, root):
      self.root=root
      self.root.title("RUET EduTrack")
      self.root.geometry("1350x700+50+30")
      self.root.config(bg="#021e2f")
      #=====background=====colors=====
      left_lbl=Label(self.root,bg="#031F3C",bd=0)
      left_lbl.place(x=0,y=0,width=600,relheight=1)

      right_lbl=Label(self.root,bg="#08A3D2",bd=0)
      right_lbl.place(x=600,y=0,relwidth=1,relheight=1)
      #==========Frame===========
      login_frame=Frame(self.root,bg="#FFFFFF")
      login_frame.place(x=150,y=100,width=1000,height=500)
      title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="#FFFFFF",fg="#08A3D2").place(x=350,y=50)

      email=Label(login_frame,text="Email Address",font=("times new roman",18,"bold"),bg="#FFFFFF",fg="gray").place(x=350,y=150)
      self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
      self.txt_email.place(x=350,y=180,width=350,height=35)


      pass_=Label(login_frame,text="Password",font=("times new roman",18,"bold"),bg="#FFFFFF",fg="gray").place(x=350,y=250)
      self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
      self.txt_pass_.place(x=350, y=280, width=350, height=35)

      def toggle_password_visibility():
          if self.txt_pass_["show"] == "*":
           self.txt_pass_["show"] = ""
          else:
           self.txt_pass_["show"] = "*"

      btn_eye = Button(login_frame, text="👁", font=("times new roman", 12),bg="lightgray", bd=0, command=toggle_password_visibility)
      btn_eye.place(x=670, y=281, width=30, height=32)


      btn_reg=Button(login_frame,text="Register New Account",font=("times new roman",14),bg="#FFFFFF",bd=0,fg="#800857",cursor="hand2",command=self.register_window).place(x=350,y=330)
      btn_forget=Button(login_frame,text="Forget Password ?",font=("times new roman",14),bg="#FFFFFF",bd=0,fg="red",cursor="hand2",command=self.forget_password_window).place(x=550,y=330)

      btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#800857",cursor="hand2",command=self.login).place(x=350,y=385,width=180,height=40)

      #=====================ruet===logo=================
      self.ruet_logo=Image.open("images/logo_ruet.png")
      self.ruet_logo=self.ruet_logo.resize((300,360),Image.Resampling.LANCZOS)
      self.ruet_logo=ImageTk.PhotoImage(self.ruet_logo)
      self.ruet_logo_lbl=Label(login_frame,image=self.ruet_logo,bg="#FFFFFF",bd=0).place(x=0,y=40,width=350,height=420)

   def reset(self):
      self.cmb_quest.current(0)
      self.txt_pass.delete(0,END)
      self.txt_new_pass.delete(0,END)
      self.txt_email.delete(0,END)
      self.txt_pass_.delete(0,END)

   def forget_password(self):
      if self.txt_otp.get() == self.var_otp.get():
         if self.txt_pass.get() == self.txt_new_pass.get():
            try:
               con = sqlite3.connect(database="rms.db")
               cur = con.cursor()
               cur.execute("update employee set password=? where email=?", (self.txt_new_pass.get(), self.txt_email.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success", "Password has been reset successfully", parent=self.root2)
               self.root2.destroy()
            except Exception as es:
               messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root2)
         else:
            messagebox.showerror("Error", "New Password and Confirm Password do not match", parent=self.root2)
      else:
         messagebox.showerror("Error", "Invalid OTP", parent=self.root2)

   def forget_password_window(self):
        if self.txt_email.get()=="" :
         messagebox.showerror("Error","Please enter the  email address to reset the password",parent=self.root)
        else:
            try:
               con=sqlite3.connect(database="rms.db")
               cur=con.cursor()
               cur.execute("select * from employee where email=?",(self.txt_email.get(),))
               row=cur.fetchone()
               if row==None:
                  messagebox.showerror("Error","Please enter the valid email address to reset the password",parent=self.root)
               else:
                  con.close()
                  self.root2=Toplevel()
                  self.root2.title("Forget Password")
                  self.root2.geometry("400x400+450+150")
                  self.root2.config(bg="white")
                  self.root2.focus_force()
                  self.root2.grab_set()
                  
                  t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                  #============forget password frame=================
                  otp=Label(self.root2,text="Enter the OTP",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=70,y=70)
                  self.txt_otp=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                  self.txt_otp.place(x=70,y=110,width=250)

                  #===================OTP=================

                  self.var_otp=StringVar()

                  answer=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=70,y=150)
                  self.txt_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                  self.txt_pass.place(x=70,y=190,width=250)

                  new_password=Label(self.root2,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=70,y=230)
                  self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                  self.txt_new_pass.place(x=70,y=270,width=250)

                  btn_change_password=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",cursor="hand2",command=self.forget_password).place(x=55,y=320,width=100,height=40)
                  btn_send_otp=Button(self.root2,text="Send OTP",font=("times new roman",15,"bold"),fg="white",bg="blue",cursor="hand2",command=self.send_otp).place(x=200,y=320,width=100,height=40)
         
         
         
            except Exception as es:
               messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

      
   def register_window(self):
      self.root.destroy()
      #import register 
      os.system("python register.py")

   def send_otp(self):
      try:
         # Generate a random 6-digit OTP
         self.var_otp.set(str(random.randint(100000, 999999)))

         # Email configuration
         #GIVE YOUR OWN INFORMATION HERE 
         #OTHERWISE OTP WILL NOT WORK
         sender_email = ""  
         sender_password = ""       
         recipient_email = self.txt_email.get()

         # Email content
         subject = "Password Reset OTP"
         message = f"Your OTP for password reset is {self.var_otp.get()}"

         # Sending email
         server = smtplib.SMTP("smtp.gmail.com", 587)
         server.starttls()
         server.login(sender_email, sender_password)
         server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")
         server.quit()

         messagebox.showinfo("Success", "OTP has been sent to your email address", parent=self.root2)
      except Exception as es:
         messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root2)

   def login(self):
      if self.txt_email.get()=="":
         messagebox.showerror("Error","Email Address is required",parent=self.root)
      elif self.txt_pass_.get()=="":
         messagebox.showerror("Error","Password is required",parent=self.root)
      else:
         try:
            con=sqlite3.connect(database="rms.db")
            cur=con.cursor()
            cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
            else:
               cur.execute("select f_name,l_name from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
               row=cur.fetchone()
               fname=row[0]
               lname=row[1]
               messagebox.showinfo("Success",f"Welcome: {fname} {lname}",parent=self.root)
               self.root.destroy()
               os.system("python dashboard.py")
             #  import dashboard
            con.close()
         except Exception as es:
            messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

root=Tk()
obj=Login_window(root)
root.mainloop()