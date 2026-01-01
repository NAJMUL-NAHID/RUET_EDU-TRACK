from tkinter import*
from PIL import Image,ImageTk #pip install pillow  
from tkinter import ttk,messagebox 
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x500+80+180")
        self.root.config(bg="white")
        self.root.focus_force()
        # title
        title=Label(self.root,text="Manage Course Details",font=("times new roman",20,"bold"),bg="#2980B9",fg="white").place(x=10,y=15,width=1230,height=40)
        #variables
        self.var_course=StringVar()

        



        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", rowheight=30)  # Set the row height to 30
        

        #====new adding course code====
        self.var_course_code=StringVar()
        self.var_credit=StringVar()
        self.var_teacher=StringVar()
        self.var_credit.set("  3.00")
        #widgets
        lbl_courseName=Label(self.root,text="Course Name",font=("times new roman",15),bg="white").place(x=10,y=70)
        lbl_coruse_code=Label(self.root,text="Course Code",font=("times new roman",15),bg="white").place(x=10,y=110)
        lbl_credit=Label(self.root,text="Credit H/R ",font=("times new roman",15),bg="white").place(x=10,y=150)
        lbl_teacher=Label(self.root,text="Course Teacher ",font=("times new roman",15),bg="white").place(x=10,y=190)
        lbl_description=Label(self.root,text="Description",font=("times new roman",15),bg="white").place(x=10,y=230)
        #entry fields
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("times new roman",15),bg="lightyellow")
        self.txt_courseName.place(x=160,y=70,width=500)
        txt_course_code=Entry(self.root,textvariable=self.var_course_code,font=("times new roman",15),bg="lightyellow").place(x=160,y=110,width=500)
        txt_credit=Entry(self.root,textvariable=self.var_credit,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=160,y=150,width=500)
        txt_teacher=Entry(self.root,textvariable=self.var_teacher,font=("times new roman",15),bg="lightyellow").place(x=160,y=190,width=500)
        self.txt_description=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_description.place(x=160,y=230,width=500,height=100)

        #buttons
        self.btn_add=Button(self.root,text="Save",font=("times new roman",15),bg="#4CAF50",fg="white",cursor="hand2",command=self.add,relief=FLAT,bd=2)
        self.btn_add.place(x=160,y=370,width=110,height=28)
        self.btn_update=Button(self.root,text="Update",font=("times new roman",15),bg="#2196F3",fg="white",cursor="hand2",command=self.update,relief=FLAT,bd=2)
        self.btn_update.place(x=280,y=370,width=110,height=28)
        self.btn_delete=Button(self.root,text="Delete",font=("times new roman",15),bg="#F44336",fg="white",cursor="hand2",command=self.delete,relief=FLAT,bd=2)
        self.btn_delete.place(x=400,y=370,width=110,height=28)
        self.btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="#9E9E9E",fg="white",cursor="hand2",command=self.clear,relief=FLAT,bd=2)
        self.btn_clear.place(x=520,y=370,width=110,height=28)
        #search panel
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Search Course | Name",font=("times new roman",15),bg="white").place(x=700,y=70)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=890,y=70,width=180)
        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="#007BFF",fg="white",cursor="hand2",command=self.search).place(x=1090,y=70,width=110,height=26)
        #content
        self.C_Frame=Frame(self.root,bd=3,relief=RIDGE)
        self.C_Frame.place(x=700,y=110,width=520,height=300)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        style = ttk.Style()
        style.configure("Treeview", rowheight=30)  # Set the row height to 30
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("code","name","credit","teacher","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("code",text="Course Code")
        self.CourseTable.heading("name",text="Course Name")
        self.CourseTable.heading("credit",text="Credit")
        self.CourseTable.heading("teacher",text="Course Teacher")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("code",width=100,anchor="center")
        self.CourseTable.column("name",width=250,anchor="center")
        self.CourseTable.column("credit",width=100,anchor="center")
        self.CourseTable.column("teacher",width=100,anchor="center")
        self.CourseTable.column("description",width=300,anchor="center")
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#============================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_course_code.set("")
        self.var_teacher.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)
        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="": 
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete this course?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course has been deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        
        self.txt_courseName.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        if not content or not content["values"]:
            return
        row=content["values"]
       # print(row)
        self.var_course.set(row[1])
        self.var_course_code.set(row[0])
        self.var_credit.set(row[2])
        self.var_teacher.set(row[3])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="": 
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course(name,code,credit,teacher,description) values(?,?,?,?,?)",(
                        self.var_course.get(),
                        self.var_course_code.get(),
                        self.var_credit.get(),
                        self.var_teacher.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course has been added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="": 
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from the list",parent=self.root)
                else:
                    cur.execute("update course set code=?, credit=?,teacher=?,description=? where name=?",(
                        self.var_course_code.get(),
                        self.var_credit.get(),
                        self.var_teacher.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course has been updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select code, name, credit, teacher, description from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
               
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select code, name, credit, teacher, description from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
               
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

            
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()