import sqlite3


conn = sqlite3.connect('sdudentGrade.db')
c = conn.cursor()



c.execute(""" 
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT,
user_type TEXT
);
""")

c.execute(""" 
CREATE TABLE IF NOT EXISTS teachers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
department TEXT
);
""")

c.execute(""" 
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
name TEXT,
age INTEGER,
department TEXT,
FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
""")

c.execute(""" 
CREATE TABLE IF NOT EXISTS marks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
studentId INTEGER,
subject TEXT,
mark INTEGER,
grade TEXT,
FOREIGN KEY(studentId) REFERENCES students(id) ON DELETE CASCADE
);
""")


def user():
    print("Welcome to Student Grade System\n User Management")
    print("1. View users")
    print("2. Add user")
    print("3. Edit user")
    print("4. Delete user")
    print("5. Dashboard")

    choices = int(input("Enter your choice: "))
    if choices == 1:
        view_user()
    elif choices == 2:
        save_user()
    elif choices == 3:
        edit_user()
    elif choices == 4:
        delete_user()
    elif choices == 5:
        dashboard()

    else:
        print("Invalid Choice")

def save_user():
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    user_type = input("Enter your user type: ")

    c.execute(""" 
    INSERT INTO users (username, password, user_type)
    VALUES (?, ?, ?)
    """, (user_name, password, user_type))
    conn.commit()

def edit_user():
    user_id = input("Enter user ID: ")
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    user_type = input("Enter your user type: ")
    c.execute(""" 
    UPDATE users
    SET username = ?, password = ?, user_type = ?
    WHERE id = ?
    """, (user_id, user_name, password, user_type))
    conn.commit()

def delete_user():
    user_id = input("Enter user ID: ")
    c.execute(""" 
    DELETE FROM users
    WHERE id = ?
    """, (user_id,))
    conn.commit()

def view_user():
    print("Welcome to Student Grade System")
    c.execute(""" 
    SELECT * FROM users
    """)
    for users in c.fetchall():
        user_id = users[0]
        username = users[1]
        password = users[2]
        user_type = users[3]
        print("Id |", "Username       |", "Password   |", "User Type")
        print(user_id,"|" ,username,"|", password,"|", user_type)

def save_teacher():
    teacher_name = input("Enter teacher's name: ")
    department = input("Enter department: ")


    c.execute(""" 
    INSERT INTO teachers (name, department)
    VALUES (?, ?)
    """, (teacher_name, department))
    conn.commit()

def edit_teacher():
    teacher_id = input("Enter teacher ID: ")
    teacher_name = input("Enter teacher's name: ")
    department = input("Enter department: ")


    c.execute(""" 
    UPDATE teachers
    SET name = ?, department = ?
    WHERE id = ?
    """, (teacher_name, department, teacher_id))
    conn.commit()

def delete_teacher():
    teacher_id = input("Enter teacher ID: ")
    c.execute(""" 
    DELETE FROM teachers
    WHERE id = ?
    """,(teacher_id,))
    conn.commit()

def view_teacher():
    print("Welcome to Student Grade System")
    c.execute(""" 
    SELECT * FROM teachers
    """)

    for teachers in c.fetchall():
        teacher_id = teachers[0]
        name = teachers[1]
        department = teachers[2]

        print("Id |", "Name       |", "Department")
        print(teacher_id,"|" ,name,"|", department)



def save_student():
    user_id = int(input("Enter user ID: "))
    student_name = input("Enter students's name: ")
    age = int(input("Enter students's age: "))
    department = input("Enter student's department: ")


    c.execute(""" 
    INSERT INTO students (user_id, name,age, department)
    VALUES (?, ?, ?, ?)
    """, (user_id, student_name, age, department))
    conn.commit()

def edit_student():
    student_id = input("Enter student ID: ")
    user_id = input("Enter user ID: ")
    student_name = input("Enter teacher's name: ")
    age = int(input("Enter students's age: "))
    department = input("Enter department: ")


    c.execute(""" 
    UPDATE students
    SET user_id = ?, name = ?, age = ?, department = ?
    WHERE id = ?
    """, (user_id, student_name, age, department, student_id))
    conn.commit()

def delete_student():
    student_id = input("Enter student ID: ")
    c.execute(""" 
    DELETE FROM students
    WHERE id = ?
    """,(student_id,))
    conn.commit()

def view_student():
    print("Welcome to Student Grade System")
    c.execute(""" 
    SELECT * FROM students
    """)

    for student in c.fetchall():
        student_id = student[0]
        user_id = student[1]
        name = student[2]
        age = student[3]
        department = student[4]

        print("Id |", "User ID  |", "Name       |","Age  |", "Department")
        print(student_id,"|", user_id,"|" ,name,"|",age,"|",department)

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B+"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C+"
    elif mark >= 40:
        return "C"
    elif mark >= 30:
        return "D+"
    else:
        return "f"

def save_mark():
    student_id = input("Enter student ID: ")
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))
    grade = calculate_grade(mark)

    c.execute(""" 
    INSERT INTO marks (studentId, subject, mark, grade)
    VALUES (?, ?, ?, ?)
    """, (student_id, subject, mark, grade))
    conn.commit()

def edit_mark():
    mark_id = input("Enter mark ID: ")
    student_id = input("Enter student ID: ")
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))
    grade = input("Enter grade: ")

    c.execute(""" 
    UPDATE marks
    SET studentID = ?, subject = ?, mark = ? , grade = ?
    WHERE id = ?
    """, (student_id, subject, mark, grade, mark_id))

    conn.commit()

def delete_mark():
    mark_id = input("Enter mark ID: ")
    c.execute(""" 
    DELETE FROM marks
    WHERE id = ?
    """, (mark_id,))

    conn.commit()

def view_grades():
    print("Welcome to Student Grade System")

    c.execute(""" 
    SELECT * FROM marks""")

    for marks in c.fetchall():
        mark_id = marks[0]
        student_id = marks[1]
        subject = marks[2]
        mark = marks[3]
        grade = marks[4]


        print("Id  |", "Student ID |", "Subject |","Mark |","Grade ")
        print(mark_id, "|", student_id, "|",subject, "|", mark, "|", grade)

def student_grades(user_id):
    try:
        print("Welcome to Student Grade System")

        c.execute("""
        SELECT students.name,
               marks.subject,
               marks.mark, 
               marks.grade
        FROM students
        JOIN marks
        ON students.id = marks.studentId       
        WHERE students.user_id = ?
        """, (user_id,))

        results = c.fetchall()
        name = results[0][0]

        print("\n====GRADE REPORT====")

        print(f"Student name: {name}")
        print("-"*40)
        print(f"{'Subject':15} {'Mark':10} {'Grade'}")

        for row in results:
            print(f"{row[1]:15} {row[2]:10} {row[3]}")

    except Exception as e:
        print(e)


def teacher():
    print("Welcome to Student Grade System\n Teacher Management")
    print("1. View teachers")
    print("2. Add teacher")
    print("3. Edit teacher")
    print("4. Delete teacher")
    print("5. Dashboard")

    choices = int(input("Enter your choice: "))
    if choices == 1:
        view_teacher()
    elif choices == 2:
        save_teacher()
    elif choices == 3:
        edit_teacher()
    elif choices == 4:
        delete_teacher()
    elif choices == 5:
        dashboard()

    else:
        print("Invalid Choice")

def students():
    print("Welcome to Student Grade System\n Student Management")
    print("1. View students")
    print("2. Add students")
    print("3. Edit students")
    print("4. Delete students")
    print("5. Dashboard")

    choices = int(input("Enter your choice: "))
    if choices == 1:
        view_student()
    elif choices == 2:
        save_student()
    elif choices == 3:
        edit_student()
    elif choices == 4:
        delete_student()
    elif choices == 5:
        dashboard()

    else:
        print("Invalid Choice")

def mark():
    print("Welcome to Student Grade System\n Mark management")

    print("1. View student marks")
    print("2. Add student mark")
    print("3. Edit student marks")
    print("4. Delete student marks")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_grades()
    elif choice == 2:
        save_mark()
    elif choice == 3:
        edit_mark()
    elif choice == 4:
        delete_mark()
    elif choice == 5:
        dashboard()
    else:
        print("Invalid Choice")

def dashboard():
    while True:
        print("Welcome to Student Grade System")
        print("1. Users")
        print("2. Teachers")
        print("3. Students")
        print("4. Marks")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            user()
        elif ch == 2:
            teacher()
        elif ch == 3:
            students()
        elif ch == 4:
            mark()
        elif ch == 5:
            break
        else:
            print("Invalid Choice")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    c.execute(""" 
    SELECT * FROM users
    WHERE username = ? AND password = ?
    """, (username, password))
    login_user = c.fetchone()

    if login_user :
        user_id = login_user[0]
        user_type = login_user[3]

        if user_type == "Student":
            print("Login Successful")
            student_grades(user_id)
        else:
            print("Login Successful")
            dashboard()
    else:
        print("Invalid username or password")

while True:
    print("Welcome to Student Grade System")
    print("1. Add user")
    print("2. Login user")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        save_user()

    elif choice == 2:
        login()

    elif choice == 3:
        break
    else:
        print("Invalid Choice")












