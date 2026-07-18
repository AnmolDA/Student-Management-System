import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_management"
)
cursor=conn.cursor()
print ("Database connected successfully")



def add_students():
    my_id=input("Enter Student ID: ")
    name=input("Enter Student Name: ")
    course=input("Enter Student course: ")
    marks=int(input("Enter Student Marks: "))

    sql="INSERT INTO student(studentID,FirstName,Course,Marks)values(%s, %s, %s, %s)" 
    values=(my_id, name, course, marks)
    cursor.execute(sql, values)
    conn.commit()
    print("Students added Successfully\n")

def view_data():
    cursor.execute("SELECT * FROM student")
    records=cursor.fetchall()
    if not records:
        print("No Student Record Found.")
        return
    for row in records:
        print(row)
        

def update_students():
    my_id=input("Enter Student ID to update: ")
    name=input("Enter New Name: ")
    course=input("Enter New Course: ")
    marks=int(input("Enter New Marks: "))

    sql="UPDATE student SET FirstName=%s,Course=%s,Marks=%s where studentID=%s"
    values=(name,course,marks,my_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Student Record Updated Successfully")
    

def delete_students():
    my_id = input("Enter Student ID to Delete: ")

    cursor.execute("DELETE FROM student WHERE studentID=%s",(my_id ,))
    conn.commit()
    print("Student Deleted Successfully")
    

while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    Choice=input("Enter Your Choice(1-5): ")
    if Choice == "1":
        add_students()
    elif Choice == "2":
        view_data()
    elif Choice == "3":
        update_students()
    elif Choice == "4":
        delete_students()
    elif Choice == "5":
        print("Program Exit Successfully")
    else:
        print("Invalid Choice...Try Again.\n")



              

