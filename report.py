from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from fpdf import FPDF
import os
class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x550+80+180")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Results", font=("times new roman", 20, "bold"), bg="#9B59B6", fg="#262626")
        title.place(x=10, y=15, width=1230, height=50)

        # Search Section and buttons   
        self.var_search = StringVar()
        self.var_search_semester = StringVar()
        lbl_search = Label(self.root, text="Roll No.", font=("times new roman", 20, "bold"), bg="white")
        lbl_search.place(x=200, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("times new roman", 20), bg="lightyellow")
        txt_search.place(x=310, y=100, width=175)

        lbl_search_semester = Label(self.root, text="Semester", font=("times new roman", 20, "bold"), bg="white")
        lbl_search_semester.place(x=500, y=100)
        self.semester_list = ["Select", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"]

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="white", background="lightyellow", bordercolor="lightyellow", arrowcolor="#9B59B6")
        
        cmb_search_semester = ttk.Combobox(self.root, textvariable=self.var_search_semester, values=self.semester_list, state="readonly", justify=CENTER, font=("times new roman", 15))
        cmb_search_semester.configure(style="TCombobox")

        cmb_search_semester.place(x=630, y=100, width=200, height=34)
        cmb_search_semester.current(0)



        btn_search = Button(self.root, text="Search", font=("times new roman", 18, "bold"), bg="#8A47A6", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=850, y=100, width=110, height=34)

        btn_clear = Button(self.root, text="Clear", font=("times new roman", 18, "bold"), bg="#5A3D8A", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=470, y=500, width=200, height=40)

        btn_generate_pdf = Button(self.root, text="Generate PDF", font=("times new roman", 18, "bold"), bg="#5A3D8A", fg="white", cursor="hand2", command=self.generate_pdf)
        btn_generate_pdf.place(x=700, y=500, width=200, height=40)

        #=====variables=====
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_semester = StringVar()
        self.var_year = StringVar()
        self.var_session = StringVar()
        self.var_course1 = StringVar()
        self.var_gpa1 = StringVar()
        self.var_course2 = StringVar()
        self.var_gpa2 = StringVar()
        self.var_course3 = StringVar()
        self.var_gpa3 = StringVar()
        self.var_course4 = StringVar()
        self.var_gpa4 = StringVar()
        self.var_course5 = StringVar()
        self.var_gpa5 = StringVar()
        self.var_totalgpa = StringVar()
        self.var_cgpa = StringVar()
        self.var_cgrade = StringVar()
        self.var_sgrade = StringVar()

        self.var_grade1 = StringVar()
        self.var_grade2 = StringVar()
        self.var_grade3 = StringVar()
        self.var_grade4 = StringVar()
        self.var_grade5 = StringVar()
        

        #=============labels  and fields  =================
        lbl_name = Label(self.root, text="Name", font=("times new roman", 15), bg="white")
        lbl_name.place(x=10, y=160)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_name.place(x=100, y=160, width=300)


        lbl_roll = Label(self.root, text="Roll No.", font=("times new roman", 15), bg="white")
        lbl_roll.place(x=420, y=160)

        txt_roll = Entry(self.root, textvariable=self.var_roll, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_roll.place(x=520, y=160, width=200)


        lbl_semester = Label(self.root, text="Semester", font=("times new roman", 15), bg="white")
        lbl_semester.place(x=10, y=200)
        txt_semester = Entry(self.root, textvariable=self.var_semester, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_semester.place(x=100, y=200, width=170)

        lbl_year = Label(self.root, text="Year", font=("times new roman", 15), bg="white")
        lbl_year.place(x=280, y=200)
        txt_year = Entry(self.root, textvariable=self.var_year, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_year.place(x=340, y=200, width=120)

        lbl_session = Label(self.root, text="Session", font=("times new roman", 15), bg="white")
        lbl_session.place(x=470, y=200)
        txt_session = Entry(self.root, textvariable=self.var_session, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_session.place(x=555, y=200, width=165)

        lbl_course1 = Label(self.root, text="Course Name", font=("times new roman", 15), bg="white")
        lbl_course1.place(x=10, y=240)
        txt_course1 = Entry(self.root, textvariable=self.var_course1, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_course1.place(x=130, y=240, width=270)


        lbl_gpa1 = Label(self.root, text="GPA", font=("times new roman", 15), bg="white")
        lbl_gpa1.place(x=410, y=240)
        txt_gpa1 = Entry(self.root, textvariable=self.var_gpa1, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_gpa1.place(x=460, y=240, width=90)
        

        lbl_grade1 = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_grade1.place(x=560, y=240)
        txt_grade1 = Entry(self.root, textvariable=self.var_grade1, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_grade1.place(x=620, y=240, width=100)


        lbl_course2 = Label(self.root, text="Course Name", font=("times new roman", 15), bg="white")
        lbl_course2.place(x=10, y=280)
        txt_course2 = Entry(self.root, textvariable=self.var_course2, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_course2.place(x=130, y=280, width=270)

        lbl_gpa2 = Label(self.root, text="GPA", font=("times new roman", 15), bg="white")
        lbl_gpa2.place(x=410, y=280)
        txt_gpa2 = Entry(self.root, textvariable=self.var_gpa2, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_gpa2.place(x=460, y=280, width=90)

        lbl_grade2 = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_grade2.place(x=560, y=280)
        txt_grade2 = Entry(self.root, textvariable=self.var_grade2, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_grade2.place(x=620, y=280, width=100)

        lbl_course3 = Label(self.root, text="Course Name", font=("times new roman", 15), bg="white")
        lbl_course3.place(x=10, y=320)
        txt_course3 = Entry(self.root, textvariable=self.var_course3, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_course3.place(x=130, y=320, width=270)

        lbl_gpa3 = Label(self.root, text="GPA", font=("times new roman", 15), bg="white")
        lbl_gpa3.place(x=410, y=320)
        txt_gpa3 = Entry(self.root, textvariable=self.var_gpa3, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_gpa3.place(x=460, y=320, width=90)

        lbl_grade3 = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_grade3.place(x=560, y=320)
        txt_grade3 = Entry(self.root, textvariable=self.var_grade3, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_grade3.place(x=620, y=320, width=100)

        lbl_course4 = Label(self.root, text="Course Name", font=("times new roman", 15), bg="white")
        lbl_course4.place(x=10, y=360)
        txt_course4 = Entry(self.root, textvariable=self.var_course4, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_course4.place(x=130, y=360, width=270)

        lbl_gpa4 = Label(self.root, text="GPA", font=("times new roman", 15), bg="white")
        lbl_gpa4.place(x=410, y=360)
        txt_gpa4 = Entry(self.root, textvariable=self.var_gpa4, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_gpa4.place(x=460, y=360, width=90)

        lbl_grade4 = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_grade4.place(x=560, y=360)
        txt_grade4 = Entry(self.root, textvariable=self.var_grade4, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_grade4.place(x=620, y=360, width=100)

        lbl_course5 = Label(self.root, text="Course Name", font=("times new roman", 15), bg="white")
        lbl_course5.place(x=10, y=400)
        txt_course5 = Entry(self.root, textvariable=self.var_course5, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_course5.place(x=130, y=400, width=270)

        lbl_gpa5 = Label(self.root, text="GPA", font=("times new roman", 15), bg="white")
        lbl_gpa5.place(x=410, y=400)
        txt_gpa5 = Entry(self.root, textvariable=self.var_gpa5, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_gpa5.place(x=460, y=400, width=90)

        lbl_grade5 = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_grade5.place(x=560, y=400)
        txt_grade5 = Entry(self.root, textvariable=self.var_grade5, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_grade5.place(x=620, y=400, width=100)

        
        # SGPA and Grade Calculation Section
        lbl_sgpa = Label(self.root, text="SGPA", font=("times new roman", 15), bg="white")
        lbl_sgpa.place(x=10, y=440)
        txt_sgpa = Entry(self.root, textvariable=self.var_totalgpa, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_sgpa.place(x=90, y=440, width=90)

        lbl_sgrade = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_sgrade.place(x=190, y=440)
        txt_sgrade = Entry(self.root, textvariable=self.var_sgrade, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_sgrade.place(x=250, y=440, width=90)
        

        # CGPA and Grade Calculation Section
        lbl_cgpa = Label(self.root, text="CGPA", font=("times new roman", 15), bg="white")
        lbl_cgpa.place(x=350, y=440)
      
        txt_cgpa = Entry(self.root, textvariable=self.var_cgpa, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_cgpa.place(x=420, y=440, width=100)

        lbl_cgrade = Label(self.root, text="Grade", font=("times new roman", 15), bg="white")
        lbl_cgrade.place(x=530, y=440)
        txt_cgrade = Entry(self.root, textvariable=self.var_cgrade, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_cgrade.place(x=620, y=440, width=100)



        # Treeview Section
        frame_tree = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame_tree.place(x=750, y=160, width=430, height=300)

        # Scrollbars
        scroll_x = Scrollbar(frame_tree, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame_tree, orient=VERTICAL)

        self.result_table = ttk.Treeview(frame_tree, columns=("roll", "semester", "name", "year", "session", "gpa1", "gpa2", "gpa3", "gpa4", "gpa5", "totalgpa", "grade"), show="headings", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)

        self.result_table.pack(fill=BOTH, expand=1)

        # Define column headings
        self.result_table.heading("roll", text="Roll No.")
        self.result_table.heading("semester", text="Semester")
        self.result_table.heading("name", text="Name")
        self.result_table.heading("year", text="Year")
        self.result_table.heading("session", text="Session")
        self.result_table.heading("gpa1", text="GPA1")
        self.result_table.heading("gpa2", text="GPA2")
        self.result_table.heading("gpa3", text="GPA3")
        self.result_table.heading("gpa4", text="GPA4")
        self.result_table.heading("gpa5", text="GPA5")
        self.result_table.heading("totalgpa", text="SGPA")
        self.result_table.heading("grade", text="Grade")
        self.result_table["show"] = "headings"
        # Define column widths
        self.result_table.column("roll", width=100, anchor="center")
        self.result_table.column("semester", width=120, anchor="center")
        self.result_table.column("name", width=250, anchor="center")
        self.result_table.column("year", width=100, anchor="center")
        self.result_table.column("session", width=120, anchor="center")
        self.result_table.column("gpa1", width=80, anchor="center")
        self.result_table.column("gpa2", width=80, anchor="center")
        self.result_table.column("gpa3", width=80, anchor="center")
        self.result_table.column("gpa4", width=80, anchor="center")
        self.result_table.column("gpa5", width=80, anchor="center")
        self.result_table.column("totalgpa", width=100, anchor="center")
        self.result_table.column("grade", width=80, anchor="center")
        self.result_table.bind("<ButtonRelease-1>",self.get_data)

    # Function to search results by roll number
    def get_data(self, ev):
        f = self.result_table.focus()
        content = (self.result_table.item(f))
        row = content['values']
        if not row:
            return
        self.var_roll.set(row[0])
        self.var_semester.set(row[1])
        self.var_name.set(row[2])
        self.var_year.set(row[3])
        self.var_session.set(row[4])
        self.var_gpa1.set(row[5])
        self.var_gpa2.set(row[6])
        self.var_gpa3.set(row[7])
        self.var_gpa4.set(row[8])
        self.var_gpa5.set(row[9])
        self.var_totalgpa.set(row[10])
        self.var_sgrade.set(row[11])
        #calculating the grade for all courses
        self.var_grade1.set(self.calculate_grade(float(row[5])))
        self.var_grade2.set(self.calculate_grade(float(row[6])))
        self.var_grade3.set(self.calculate_grade(float(row[7])))
        self.var_grade4.set(self.calculate_grade(float(row[8])))
        self.var_grade5.set(self.calculate_grade(float(row[9])))

        #getting the course names from the database
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select course1,course2,course3,course4,course5 from student where roll=? and semester=?", (row[0], row[1]))
            rows = cur.fetchall()
            if len(rows) > 0:
                self.var_course1.set(rows[0][0])
                self.var_course2.set(rows[0][1])
                self.var_course3.set(rows[0][2])
                self.var_course4.set(rows[0][3])
                self.var_course5.set(rows[0][4])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        self.calculate_cgpa()  # Calculate CGPA when a row is selected

    def generate_pdf(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
               messagebox.showerror("Error", "Please select a student record to generate PDF", parent=self.root)
               return

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Title
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt="Student Result Report RUET", ln=True, align="C")
            pdf.ln(10)

            # Student Information
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Name: {self.var_name.get()}", ln=True)
            pdf.cell(200, 10, txt=f"Roll No: {self.var_roll.get()}", ln=True)
            pdf.cell(200, 10, txt=f"Semester: {self.var_semester.get()}", ln=True)
            pdf.cell(200, 10, txt=f"Year: {self.var_year.get()}", ln=True)
            pdf.cell(200, 10, txt=f"Session: {self.var_session.get()}", ln=True)
            pdf.ln(10)

            # Course and GPA Details
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(110, 10, txt="Course Name", border=1, align="C")
            pdf.cell(40, 10, txt="GPA", border=1, align="C")
            pdf.cell(40, 10, txt="Grade", border=1, align="C")
            pdf.ln()

            pdf.set_font("Arial", size=12)
            courses = [
            (self.var_course1.get(), self.var_gpa1.get(), self.var_grade1.get()),
            (self.var_course2.get(), self.var_gpa2.get(), self.var_grade2.get()),
            (self.var_course3.get(), self.var_gpa3.get(), self.var_grade3.get()),
            (self.var_course4.get(), self.var_gpa4.get(), self.var_grade4.get()),
            (self.var_course5.get(), self.var_gpa5.get(), self.var_grade5.get()),
            ]
            for course, gpa, grade in courses:
             if course:  # Only include non-empty courses
                pdf.cell(110, 10, txt=course, border=1)
                pdf.cell(40, 10, txt=gpa, border=1, align="C")
                pdf.cell(40, 10, txt=grade, border=1, align="C")
                pdf.ln()

            # SGPA and CGPA
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"SGPA: {self.var_totalgpa.get()} | Grade: {self.var_sgrade.get()}",ln=True)
            pdf.cell(200, 10, txt=f"CGPA: {self.var_cgpa.get()} | Grade: {self.var_cgrade.get()}", ln=True)

            # Save PDF
            output_folder = "Result Sheets"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            pdf_file = os.path.join(output_folder, f"{self.var_roll.get()}_{self.var_semester.get()}_result.pdf")
            pdf.output(pdf_file)
            messagebox.showinfo("Success", f"PDF generated successfully: {pdf_file}", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error while generating PDF: {str(ex)}", parent=self.root)
        finally:
            con.close()




    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Please enter roll number", parent=self.root)
                return
            elif self.var_search_semester.get() == "Select":
                cur.execute("select roll,semester,name,year, session ,gpa1,gpa2,gpa3,gpa4,gpa5,totalgpa,grade from result where roll=?", (self.var_search.get(),))
                rows = cur.fetchall()
                if len(rows) > 0:
                    self.result_table.delete(*self.result_table.get_children())  # Clear previous data
                    for row in rows:
                        self.result_table.insert("", END, values=row)  # Insert new data
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
            else:
                cur.execute("select roll,semester,name,year, session ,gpa1,gpa2,gpa3,gpa4,gpa5,totalgpa,grade from result where roll=? and semester=?", (self.var_search.get(), self.var_search_semester.get()))
                rows = cur.fetchall()
                if len(rows) > 0:
                    self.result_table.delete(*self.result_table.get_children())
                    for row in rows:
                        self.result_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Function to clear the search field and Treeview
    def clear(self):
        self.var_search.set("")
        self.result_table.delete(*self.result_table.get_children())  # Clear Treeview data
        self.var_search_semester.set("Select")
        self.var_roll.set("")
        self.var_semester.set("")
        self.var_name.set("")
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
        self.var_totalgpa.set("")
        self.var_sgrade.set("")
        self.var_cgpa.set("")
        self.var_cgrade.set("")
        self.var_grade1.set("")
        self.var_grade2.set("")
        self.var_grade3.set("")
        self.var_grade4.set("")
        self.var_grade5.set("")


    def calculate_cgpa(self):
        try:
            # Retrieve SGPA values
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("select totalgpa,totalcredit from result where roll=?", (self.var_roll.get(),))
            sgpa_rows = cur.fetchall()
            sgpa_sum = 0.0
            total_credit_sum = 0.0
            if len(sgpa_rows) > 0:
                for sgpa in sgpa_rows:
                    sgpa_sum += float(sgpa[0])* float(sgpa[1])
                    total_credit_sum += float(sgpa[1])
                cgpa = sgpa_sum / total_credit_sum if total_credit_sum > 0 else 0.0
            self.var_cgpa.set(f"{cgpa:.2f}")  # Set CGPA with 2 decimal places

            # Calculate Grade
            grade = self.calculate_grade(cgpa)
            self.var_cgrade.set(grade)

        except Exception as ex:
            messagebox.showerror("Error", f"Error while calculating CGPA: {str(ex)}", parent=self.root)



    def calculate_grade(self, gpa):
        # Function to calculate grade based on CGPA
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
        


if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()