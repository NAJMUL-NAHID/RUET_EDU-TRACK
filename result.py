from tkinter import*
from PIL import Image,ImageTk #pip install pillow  
from tkinter import ttk,messagebox 
from student import StudentClass
import sqlite3
class ResultClass:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x600+80+180")
        self.root.config(bg="white")
        self.root.focus_force()
        # title
        title=Label(self.root,text="Add Student Results",font=("times new roman",20,"bold"),bg="#E67E22",fg="#262626").place(x=10,y=15,width=1230,height=50)
        #====widgets=====

        #====variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_semester=StringVar() 
        self.var_year=StringVar()
        self.var_session=StringVar()

        #================================
        
        self.var_course1=StringVar()
        self.var_gpa1=StringVar()
        self.var_course2=StringVar()
        self.var_gpa2=StringVar()
        self.var_course3=StringVar()
        self.var_gpa3=StringVar()
        self.var_course4=StringVar()
        self.var_gpa4=StringVar()
        self.var_course5=StringVar()
        self.var_gpa5=StringVar()
        self.var_gpa=StringVar()
        self.var_grade=StringVar()
        

        self.roll_list=[]
        self.fetch_roll()
       

        lbl_select=Label(self.root,text="Select Student",font=("times new roman",15),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=180)
        lbl_semester=Label(self.root,text="Semester",font=("times new roman",15),bg="white").place(x=50,y=140)
        lbl_year=Label(self.root,text="Year",font=("times new roman",15),bg="white").place(x=50,y=220)
        lbl_session=Label(self.root,text="Session",font=("times new roman",15),bg="white").place(x=50,y=260)



        #====combobox=====
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="white", background="lightyellow", bordercolor="lightyellow", arrowcolor="blue")
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("times new roman",15),state="readonly",justify=CENTER)
        self.txt_student.place(x=250,y=100,width=410)
        self.txt_student.set("Select")



        # Semester Dropdown
        self.semester_list = ["Select", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"]
        self.txt_semester = ttk.Combobox(self.root, textvariable=self.var_semester, values=self.semester_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_semester.place(x=250,y=140,width=250)
        self.txt_semester.current(0)
        
        

        btn_search=Button(self.root,text="Search",font=("times new roman",15),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=510,y=140,width=150,height=28)


        


        #=====entry fields=====
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow",state="readonly",justify=CENTER).place(x=250,y=180,width=410)        

      
    
        self.txt_year=Entry(self.root,textvariable=self.var_year,font=("times new roman",15),bg="lightyellow").place(x=250,y=220,width=410)
        self.txt_session=Entry(self.root,textvariable=self.var_session,font=("times new roman",15),bg="lightyellow")
        self.txt_session.place(x=250,y=260,width=410)
        

        #====marks===== 
        lbl_course1=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=50,y=300)
        self.txt_course1 = Entry(self.root, textvariable=self.var_course1, font=("times new roman", 15), bg="lightyellow", state="readonly")
        self.txt_course1.place(x=250, y=300, width=200)
        lbl_gpa1=Label(self.root,text="GPA",font=("times new roman",15),bg="white").place(x=470,y=300)
        self.txt_gpa1 = Entry(self.root, textvariable=self.var_gpa1, font=("times new roman", 15), bg="lightyellow")
        self.txt_gpa1.place(x=550, y=300, width=110)
        
        lbl_course2=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=50,y=340)
        self.txt_course2 = Entry(self.root, textvariable=self.var_course2, font=("times new roman", 15), bg="lightyellow", state="readonly")
        self.txt_course2.place(x=250, y=340, width=200)
        lbl_gpa2=Label(self.root,text="GPA",font=("times new roman",15),bg="white").place(x=470,y=340)
        self.txt_gpa2 = Entry(self.root, textvariable=self.var_gpa2, font=("times new roman", 15), bg="lightyellow")
        self.txt_gpa2.place(x=550, y=340, width=110)


        lbl_course3=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=50,y=380)
        self.txt_course3 = Entry(self.root, textvariable=self.var_course3, font=("times new roman", 15), bg="lightyellow", state="readonly")
        self.txt_course3.place(x=250, y=380, width=200)
        lbl_gpa3=Label(self.root,text="GPA",font=("times new roman",15),bg="white").place(x=470,y=380)
        self.txt_gpa3 = Entry(self.root, textvariable=self.var_gpa3, font=("times new roman", 15), bg="lightyellow")
        self.txt_gpa3.place(x=550, y=380, width=110)

        lbl_course4=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=50,y=420)
        self.txt_course4 = Entry(self.root, textvariable=self.var_course4, font=("times new roman", 15), bg="lightyellow", state="readonly")
        self.txt_course4.place(x=250, y=420, width=200)
        lbl_gpa4=Label(self.root,text="GPA",font=("times new roman",15),bg="white").place(x=470,y=420)
        self.txt_gpa4 = Entry(self.root, textvariable=self.var_gpa4, font=("times new roman", 15), bg="lightyellow")
        self.txt_gpa4.place(x=550, y=420, width=110)

        lbl_course5=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=50,y=460)
        self.txt_course5 = Entry(self.root, textvariable=self.var_course5, font=("times new roman", 15), bg="lightyellow", state="readonly")
        self.txt_course5.place(x=250, y=460, width=200)
        lbl_gpa5=Label(self.root,text="GPA",font=("times new roman",15),bg="white").place(x=470,y=460)
        self.txt_gpa5 = Entry(self.root, textvariable=self.var_gpa5, font=("times new roman", 15), bg="lightyellow")
        self.txt_gpa5.place(x=550, y=460, width=110)


        lbl_gpa=Label(self.root,text="Total Gpa",font=("times new roman",15),bg="white").place(x=50,y=500)
        self.txt_total_gpa = Entry(self.root, textvariable=self.var_gpa, font=("times new roman", 15), bg="lightyellow")
        self.txt_total_gpa.place(x=250, y=500, width=200)
        self.txt_total_gpa.config(state="readonly")
        

        lbl_grade=Label(self.root,text="Grade",font=("times new roman",15),bg="white").place(x=470,y=500)
        self.txt_grade = Entry(self.root, font=("times new roman", 15), bg="lightyellow",textvariable=self.var_grade)
        self.txt_grade.place(x=550, y=500, width=110)
        self.txt_grade.config(state="readonly")













        #====buttons=====
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=250,y=550,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=370,y=550,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",font=("times new roman",15),bg="red",activebackground="red",cursor="hand2",command=self.delete).place(x=490,y=550,width=110,height=35)


        #====content=====
        #====images=====
        self.bg_img=Image.open("images/result_image.png")
        self.bg_img=self.bg_img.resize((500,460),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=670,y=100,width=500,height=380)

#================================================================

    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
            self.roll_list = list(set(self.roll_list))
            self.roll_list.sort()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="Select" or self.var_semester.get()=="Select" or self.var_year.get()=="":
                messagebox.showerror("Error","Please provide roll , semester and year",parent=self.root)
                return
            cur.execute("select * from result where roll=? and semester=? and year=?", (self.var_roll.get(), self.var_semester.get(), self.var_year.get()))
            row = cur.fetchone()
            if row != None:
                op=messagebox.askyesno("Confirm","Do you want to delete this result ?",parent=self.root)
                if op==True:
                    cur.execute("delete from result where roll=? and semester=? and year=?", (self.var_roll.get(), self.var_semester.get(), self.var_year.get()))
                    con.commit()
                    messagebox.showinfo("Delete","Result deleted successfully",parent=self.root)
                    self.clear()
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

                

    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select course1 ,course2, course3,course4,course5 from student where roll=? and semester=?",(self.var_roll.get(),self.var_semester.get()))
            row=cur.fetchone()
            if row!=None:
                self.txt_session.config(state="readonly")
                self.txt_course1.config(state="readonly")
                self.txt_course2.config(state="readonly")
                self.txt_course3.config(state="readonly")
                self.txt_course4.config(state="readonly")
                self.txt_course5.config(state="readonly")
                self.var_course1.set(row[0])
                self.var_course2.set(row[1])
                self.var_course3.set(row[2])
                self.var_course4.set(row[3])
                self.var_course5.set(row[4])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
          
          
    
    def search(self):
        if self.var_roll.get()=="Select" or self.var_semester.get()=="Select":
            messagebox.showerror("Error", "Please select roll and semester", parent=self.root)
            return
        self.clear_search()
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name , session from student where roll=? and semester=?",(self.var_roll.get(),self.var_semester.get()))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_session.set(row[1])
                self.fetch_course()
                self.fetch_result()
            else:  
                messagebox.showerror("Error","No record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    


    def fetch_result(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from result where roll=? and semester=?",(self.var_roll.get(),self.var_semester.get()))
            row=cur.fetchone()
            if row!=None:
                self.var_gpa1.set(row[6])
                self.var_gpa2.set(row[7])
                self.var_gpa3.set(row[8])
                self.var_gpa4.set(row[9])
                self.var_gpa5.set(row[10])
                self.var_gpa.set(row[11])
                self.var_grade.set(row[12])
                self.var_year.set(row[4])
                self.var_session.set(row[5])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="" : 
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            elif self.var_year.get()=="" or self.var_session.get()=="":
                messagebox.showerror("Error","Please enter year and session",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and semester=? and year=?", (self.var_roll.get(), self.var_semester.get(), self.var_year.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result already present for this student in the selected semester and year", parent=self.root)
                    return
                else:
                    if not all([self.var_gpa1.get(), self.var_gpa2.get(), self.var_gpa3.get(), self.var_gpa4.get(), self.var_gpa5.get()]):
                        messagebox.showerror("Error", "Please enter GPA for all courses", parent=self.root)
                        return
                    else:
                        var_total_credit=0.0
                        var_total_gpa=0.0
                        if float(self.var_gpa1.get())<2.0:
                            self.var_gpa1.set("0.0")
                            var_total_credit+=0.0
                        else:
                            var_total_credit+=3.0
                            var_total_gpa+=float(self.var_gpa1.get())*3.0

                        if float(self.var_gpa2.get())<2.0:
                            self.var_gpa2.set("0.0")
                            var_total_credit+=0.0
                        else:
                            var_total_credit+=3.0
                            var_total_gpa+=float(self.var_gpa2.get())*3.0

                        if float(self.var_gpa3.get())<2.0:
                            self.var_gpa3.set("0.0")
                            var_total_credit+=0.0
                        else:
                            var_total_credit+=3.0
                            var_total_gpa+=float(self.var_gpa3.get())*3.0

                        if float(self.var_gpa4.get())<2.0:
                            self.var_gpa4.set("0.0")
                            var_total_credit+=0.0
                        else:
                            var_total_credit+=3.0
                            var_total_gpa+=float(self.var_gpa4.get())*3.0

                        if float(self.var_gpa5.get())<2.0:
                            self.var_gpa5.set("0.0")
                            var_total_credit+=0.0
                        else:
                            var_total_credit+=3.0
                            var_total_gpa+=float(self.var_gpa5.get())*3.0
                    
                        self.var_gpa.set("{:.2f}".format((var_total_gpa/var_total_credit)))
                        self.var_grade.set(self.calculate_grade())
                        cur.execute("insert into result(roll,semester,name,year, session ,gpa1,gpa2,gpa3,gpa4,gpa5,totalgpa,grade,totalcredit) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                            self.var_roll.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_year.get(),
                            self.var_session.get(),
                            self.var_gpa1.get(),
                            self.var_gpa2.get(),
                            self.var_gpa3.get(),
                            self.var_gpa4.get(),
                            self.var_gpa5.get(),
                            self.var_gpa.get(),
                            self.var_grade.get(),
                            str(var_total_credit)
                            
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Result has been added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_semester.set("Select")
        self.var_year.set("")
        self.var_session.set("")
        self.var_course1.set("")
        self.var_gpa1.set("")
        self.var_course2.set("")
        self.var_gpa2.set("")
        self.var_course3.set("")
        self.var_gpa3.set("")
        self.var_course4.set("")
        self.var_gpa4.set("")
        self.var_course5.set("")
        self.var_gpa5.set("")
        self.var_gpa.set("")
        self.var_grade.set("")
        self.txt_student.set("Select")
        self.txt_semester.current(0)
    def clear_search(self):
        self.var_name.set("")
        self.var_session.set("")
        self.var_course1.set("")
        self.var_gpa1.set("")
        self.var_course2.set("")
        self.var_gpa2.set("")
        self.var_course3.set("")
        self.var_gpa3.set("")
        self.var_course4.set("")
        self.var_gpa4.set("")
        self.var_course5.set("")
        self.var_gpa5.set("")
        self.var_gpa.set("")
        self.var_grade.set("")
    
    def calculate_grade(self):
        gpa = float(self.var_gpa.get())
        if gpa >= 4.00:
            return "A+"
        elif gpa >= 3.75:
            return "A"
        elif gpa >= 3.50:
            return "A-"
        elif gpa >= 3.25:
            return "B+"
        elif gpa >= 3.00:
            return "B"
        elif gpa >= 2.75:
            return "B-"
        elif gpa >= 2.50:
            return "C+"
        elif gpa >= 2.25:
            return "C"
        elif gpa >= 2.00:
            return "C-"
        else:
            return "F"
        
if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()