import sqlite3

def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,code text, credit text, teacher text, description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(sid INTEGER PRIMARY KEY AUTOINCREMENT, roll INTEGER, name text, email text, gender text, session text, contact text, admission text, course1 text, course2 text, course3 text, course4 text, course5 text,semester text, state text, city text, address text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,semester text, name text, year text, session text, gpa1 text,gpa2 text ,gpa3 text,gpa4 text,gpa5 text, totalgpa text,grade text, totalcredit text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()
    con.close()
create_db()
