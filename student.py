from tkinter import*    
from PIL import Image,ImageTk #pip install pillow  
from tkinter import ttk,messagebox 
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x600+80+180")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Manage Student Details",font=("times new roman",20,"bold"),bg="#16A085",fg="white").place(x=10,y=15,width=1230,height=40)
       
       
        #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_session=StringVar()
        self.var_contact=StringVar()
        self.var_course1=StringVar()
        self.var_course2=StringVar()
        self.var_course3=StringVar()
        self.var_course4=StringVar()
        self.var_course5=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_semester=StringVar() 
        
        #widgets
        #=====column 1==================
        lbl_roll=Label(self.root,text="Roll No. ",font=("times new roman",15),bg="white").place(x=10,y=70)
        lbl_Name=Label(self.root,text="Name ",font=("times new roman",15),bg="white").place(x=10,y=110)
        lbl_Email=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=10,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=10,y=190)



        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=10,y=360)


        #entry fields for column 1
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("times new roman",15),bg="lightyellow")
        self.txt_roll.place(x=160,y=70,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=160,y=110,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="lightyellow").place(x=160,y=150,width=200)


        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="white", background="lightyellow", bordercolor="lightyellow", arrowcolor="#16A085")


        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),font=("times new roman",15),state="readonly",justify=CENTER)
        self.txt_gender.place(x=160,y=190,width=100)
        self.txt_gender.current(0)

        #=====column 2==================
        lbl_session=Label(self.root,text="Session",font=("times new roman",15),bg="white").place(x=370,y=70)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=370,y=110)
        lbl_admission=Label(self.root,text="Admission",font=("times new roman",15),bg="white").place(x=370,y=150)
        
        lbl_state=Label(self.root,text="Country",font=("times new roman",15),bg="white").place(x=270,y=190)
        self.txt_state=Entry(self.root,textvariable=self.var_state,font=("times new roman",15),bg="lightyellow").place(x=340,y=190,width=150)

        lbl_city=Label(self.root,text="City",font=("times new roman",15),bg="white").place(x=495,y=190)
        self.txt_city=Entry(self.root,textvariable=self.var_city,font=("times new roman",15),bg="lightyellow").place(x=550,y=190,width=140)

        #===========courses=================
        self.course_list = ["Select"]
        self.fetch_course()


        lbl_course1 = Label(self.root, text="Course 1", font=("times new roman", 15), bg="white").place(x=10, y=240)
        self.txt_course1 = ttk.Combobox(self.root, textvariable=self.var_course1, values=self.course_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_course1.place(x=160, y=240, width=200)
        self.txt_course1.current(0)

        lbl_course2 = Label(self.root, text="Course 2", font=("times new roman", 15), bg="white").place(x=370, y=240)
        self.txt_course2 = ttk.Combobox(self.root, textvariable=self.var_course2, values=self.course_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_course2.place(x=490, y=240, width=200)
        self.txt_course2.current(0)

        lbl_course3 = Label(self.root, text="Course 3", font=("times new roman", 15), bg="white").place(x=10, y=280)
        self.txt_course3 = ttk.Combobox(self.root, textvariable=self.var_course3, values=self.course_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_course3.place(x=160, y=280, width=200)
        self.txt_course3.current(0)

        lbl_course4 = Label(self.root, text="Course 4", font=("times new roman", 15), bg="white").place(x=370, y=280)
        self.txt_course4 = ttk.Combobox(self.root, textvariable=self.var_course4, values=self.course_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_course4.place(x=490, y=280, width=200)
        self.txt_course4.current(0)

        lbl_course5 = Label(self.root, text="Course 5", font=("times new roman", 15), bg="white").place(x=10, y=320)
        self.txt_course5 = ttk.Combobox(self.root, textvariable=self.var_course5, values=self.course_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_course5.place(x=160, y=320, width=200)
        self.txt_course5.current(0)
        
       
        # Semester Label and Entry Field
        # Semester List
        self.semester_list = ["Select", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"]

        # Semester Dropdown
        lbl_semester = Label(self.root, text="Semester", font=("times new roman", 15), bg="white").place(x=370, y=320)
        self.txt_semester = ttk.Combobox(self.root, textvariable=self.var_semester, values=self.semester_list, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_semester.place(x=490, y=320, width=200)
        self.txt_semester.current(0)
        
        #entry fields for column  2
       
        
        self.txt_sesion=Entry(self.root,textvariable=self.var_session,font=("times new roman",15),bg="lightyellow").place(x=490,y=70,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=490,y=110,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("times new roman",15),bg="lightyellow").place(x=490,y=150,width=200)
      


        #=============txt address==================

        self.txt_address=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_address.place(x=160,y=360,width=530,height=100)

        #buttons
        self.btn_add=Button(self.root,text="Save",font=("Helvetica",15,"bold"),bg="#4CAF50",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=160,y=520,width=110,height=28)
        self.btn_update=Button(self.root,text="Update",font=("Helvetica",15,"bold"),bg="#2196F3",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=280,y=520,width=110,height=28)
        self.btn_delete=Button(self.root,text="Delete",font=("Helvetica",15,"bold"),bg="#F44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=400,y=520,width=110,height=28)
        self.btn_clear=Button(self.root,text="Clear",font=("Helvetica",15,"bold"),bg="#9E9E9E",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=520,y=520,width=110,height=28)
        #search panel
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No. ",font=("times new roman",15),bg="white").place(x=700,y=70)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=890,y=70,width=180)
        btn_search=Button(self.root,text="Search",font=("Helvetica",14,"bold"),bg="#007BFF",fg="white",cursor="hand2",command=self.search).place(x=1090,y=70,width=110,height=26)
        #content
        self.C_Frame=Frame(self.root,bd=3,relief=RIDGE)
        self.C_Frame.place(x=700,y=110,width=520,height=300)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","session","contact","admission","course1","course2","course3","course4","course5","semester","state","city","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("session", text="Session")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course1", text="Course 1")
        self.CourseTable.heading("course2", text="Course 2")
        self.CourseTable.heading("course3", text="Course 3")
        self.CourseTable.heading("course4", text="Course 4")
        self.CourseTable.heading("course5", text="Course 5")
        self.CourseTable.heading("semester", text="Semester")
        self.CourseTable.heading("state", text="Country")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("address", text="Address")
        
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("roll", width=100, anchor=CENTER)
        self.CourseTable.column("name", width=250, anchor=CENTER)
        self.CourseTable.column("email", width=200, anchor=CENTER)
        self.CourseTable.column("gender", width=100, anchor=CENTER)
        self.CourseTable.column("session", width=100, anchor=CENTER)
        self.CourseTable.column("contact", width=120, anchor=CENTER)
        self.CourseTable.column("admission", width=120, anchor=CENTER)
        self.CourseTable.column("course1", width=250, anchor=CENTER)
        self.CourseTable.column("course2", width=250, anchor=CENTER)
        self.CourseTable.column("course3", width=250, anchor=CENTER)
        self.CourseTable.column("course4", width=250, anchor=CENTER)
        self.CourseTable.column("course5", width=250, anchor=CENTER)
        self.CourseTable.column("semester", width=120, anchor=CENTER)
        self.CourseTable.column("state", width=100, anchor=CENTER)
        self.CourseTable.column("city", width=100, anchor=CENTER)
        self.CourseTable.column("address", width=200, anchor=CENTER)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#============================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_session.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course1.set("Select")
        self.var_course2.set("Select")
        self.var_course3.set("Select")
        self.var_course4.set("Select")
        self.var_course5.set("Select")
        self.var_semester.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
            
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="" or self.var_semester.get()=="Select": 
                messagebox.showerror("Error","Roll No. and semester required",parent=self.root)
            else:
                cur.execute("select * from student where roll=? AND semester=?", (self.var_roll.get(), self.var_semester.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete this student?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=? and semester=?",(self.var_roll.get(),self.var_semester.get()))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        
        if not content or not content["values"]:
            return
        row=content["values"]
        # print(row)
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_session.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course1.set(row[7])
        self.var_course2.set(row[8])
        self.var_course3.set(row[9])
        self.var_course4.set(row[10])
        self.var_course5.set(row[11])
        self.var_semester.set(row[12])
        self.var_state.set(row[13])
        self.var_city.set(row[14])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[15])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="" or self.var_semester.get()=="Select": 
                messagebox.showerror("Error","Roll No. and semester are required",parent=self.root)
            else:
                cur.execute("select * from student where roll=? and semester=?",(self.var_roll.get(),self.var_semester.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","The Student is already admitted in this semester",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,session,contact,admission,course1,course2,course3,course4,course5,semester,state,city,address) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_session.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course1.get(),
                        self.var_course2.get(),
                        self.var_course3.get(),
                        self.var_course4.get(),
                        self.var_course5.get(),
                        self.var_semester.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student has been added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="" or self.var_semester.get()=="Select": 
                messagebox.showerror("Error","Roll No. and semester should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=? AND semester=?",(self.var_roll.get(),self.var_semester.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Student from the list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,session=?,contact=?,admission=?,course1=?,course2=?,course3=?,course4=?,course5=?,semester=?,state=?,city=?,address=? where roll=? and semester=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_session.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course1.get(),
                        self.var_course2.get(),
                        self.var_course3.get(),
                        self.var_course4.get(),
                        self.var_course5.get(),
                        self.var_semester.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get(),
                        self.var_semester.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student has been updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll, name, email, gender, session, contact, admission, course1, course2, course3, course4, course5, semester, state, city, address from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll, name, email, gender, session, contact, admission, course1, course2, course3, course4, course5, semester, state, city, address from student where roll=?", (self.var_search.get(),))
            rows=cur.fetchall()
            if len(rows)>0:
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)
            else:  
                messagebox.showerror("Error","No record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()