from tkinter import*
from PIL import Image,ImageTk #pip install pillow  
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import os
from tkinter import *
from PIL import Image, ImageTk
from datetime import*
from math import*
import sqlite3
from tkinter import messagebox
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Dashboard")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#f0f0f0")  # Set a light gray background for a modern look
        #icon
        # Resize the logo image
        logo_image = Image.open("images/logo_ruet.png")
        logo_image = logo_image.resize((50, 50), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing # Resize to 50x50 pixels
        self.logo_dash=ImageTk.PhotoImage(logo_image)  # Create a PhotoImage object


      
        # title
        title=Label(self.root,text="RUET EduTrack",compound=LEFT,padx=10,image=self.logo_dash,font=("Helvetica",22,"bold"),bg="#2C3E50",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=1160,y=55,width=350,height=800)

        # Extra Frame

        lbl_menu_info = Label(M_Frame, text="Quick Links", font=("Helvetica", 15, "bold"), bg="white", fg="#2C3E50")
        lbl_menu_info.place(x=20, y=400)

        # Buttons for website links
        btn_link1 = Button(M_Frame, text="RUET Official", font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", 
            activebackground="#2980B9", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start https://www.ruet.ac.bd"))
        btn_link1.place(x=20, y=440, width=300, height=30)

        btn_link2 = Button(M_Frame, text="RUET CSE", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="white", 
            activebackground="#16A085", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start https://www.cse.ruet.ac.bd"))
        btn_link2.place(x=20, y=478, width=300, height=30)

        btn_link3 = Button(M_Frame, text="RUET Library", font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", 
            activebackground="#E67E22", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start https://library.ruet.ac.bd"))
        btn_link3.place(x=20, y=516, width=300, height=30)

        btn_link4 = Button(M_Frame, text="RAPL Website", font=("Helvetica", 12, "bold"), bg="#000000", fg="white", 
            activebackground="#C0392B", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start https://rapl.site"))
        btn_link4.place(x=20, y=554, width=300, height=30)

        btn_email = Button(M_Frame, text="Email Me", font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", 
            activebackground="#C0392B", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start mailto:nahidmulla777777@gmail.com"))
        btn_email.place(x=20, y=592, width=300, height=30)

        btn_github = Button(M_Frame, text="My GitHub", font=("Helvetica", 12, "bold"), bg="#6C3483", fg="white", 
            activebackground="#5B2C6F", activeforeground="white", cursor="hand2", 
            command=lambda: os.system("start https://github.com/najmul-nahid"))
        btn_github.place(x=20, y=630, width=300, height=30)

        #buttons
        btn_course=Button(M_Frame,text="Course",font=("Helvetica",15,"bold"),bg="#3498DB",fg="white",activebackground="#2980B9",activeforeground="white",cursor="hand2",command=self.add_course).place(x=20,y=20,width=300,height=45)
        btn_student=Button(M_Frame,text="Student",font=("Helvetica",15,"bold"),bg="#1ABC9C",fg="white",activebackground="#16A085",activeforeground="white",cursor="hand2",command=self.add_student).place(x=20,y=80,width=300,height=45)
        btn_result=Button(M_Frame,text="Add result",font=("Helvetica",15,"bold"),bg="#F39C12",fg="white",activebackground="#E67E22",activeforeground="white",cursor="hand2",command=self.add_result).place(x=20,y=140,width=300,height=45)
        btn_view_result=Button(M_Frame,text="View Result",font=("Helvetica",15,"bold"),bg="#9B59B6",fg="white",activebackground="#8E44AD",activeforeground="white",cursor="hand2",command=self.add_report).place(x=20,y=200,width=300,height=45)
        btn_logout=Button(M_Frame,text="Logout",font=("Helvetica",15,"bold"),bg="#FF5733",fg="white",activebackground="#C0392B",activeforeground="white",cursor="hand2",command=self.logout).place(x=20,y=260,width=300,height=45)
        btn_exit=Button(M_Frame,text="Exit",font=("Helvetica",15,"bold"),bg="#C0392B",fg="white",activebackground="#C0392B",activeforeground="white",cursor="hand2",command=self.exit).place(x=20,y=320,width=300,height=45)
        self.bg_img=Image.open("images/RUET_bg.jpg")
        self.bg_img=self.bg_img.resize((1350,650),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=5,y=55,width=1150,height=550)
        
        #update_details
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("Helvetica",20,"bold"),bd=10,relief=FLAT,bg="#3498DB",fg="white",anchor="center")
        self.lbl_course.place(x=5,y=610,width=375,height=135)

        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("Helvetica",20,"bold"),bd=10,relief=FLAT,bg="#1ABC9C",fg="white",anchor="center")
        self.lbl_student.place(x=390,y=610,width=375,height=135)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("Helvetica",20,"bold"),bd=10,relief=FLAT,bg="#F39C12",fg="white",anchor="center")
        self.lbl_result.place(x=780,y=610,width=375,height=135)

        #footer
        footer=Label(self.root,text="Developed by JNS Technologies Limited  \n For any inconvenience contact us at 01616026009  ",font=("times new roman",15),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#===========================================================    
    
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
    
            cur.execute("select distinct roll from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            
            
            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
  
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm","Are you sure you want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm","Are you sure you want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()