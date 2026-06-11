STUDENT GRADE SYSTEM

Project Report

Submitted By

Abdu Rahoof

Technology Used

* Python 3
* SQLite3 Database

⸻

1. Introduction

Student Grade System is a database-driven application developed using Python and SQLite. The system helps manage student information, teacher information, user accounts, and student grades.

The project provides role-based access control. Administrators can manage users, teachers, students, and marks. Students can log in and view only their own grades. This ensures data security and privacy.

The system automates grade calculation based on marks entered by the administrator.

⸻

2. Objectives

The main objectives of this project are:

* To manage student records efficiently.
* To manage teacher information.
* To maintain user login authentication.
* To store student marks securely.
* To calculate grades automatically.
* To provide role-based access control.
* To allow students to view only their own academic results.

⸻

3. Scope of the Project

The Student Grade System can be used in schools, colleges, and educational institutions for managing student records and grades.

The system provides:

* User Management
* Teacher Management
* Student Management
* Mark Management
* Grade Calculation
* Login Authentication

⸻

4. System Requirements

Hardware Requirements

* Computer/Laptop
* Minimum 4 GB RAM
* 100 MB Free Disk Space

Software Requirements

* Python 3.x
* SQLite3
* VS Code / PyCharm / IDLE

⸻

5. Database Design

Table: users

Field	Type
id	INTEGER
username	TEXT
password	TEXT
user_type	TEXT

⸻

Table: teachers

Field	Type
id	INTEGER
name	TEXT
department	TEXT

⸻

Table: students

Field	Type
id	INTEGER
user_id	INTEGER
name	TEXT
age	INTEGER
department	TEXT

⸻

Table: marks

Field	Type
id	INTEGER
studentId	INTEGER
subject	TEXT
mark	INTEGER
grade	TEXT

⸻

6. ER Diagram

+-----------+
|   USERS   |
+-----------+
| id        |
| username  |
| password  |
| user_type |
+-----------+
      |
      |
      v
+-------------+
|  STUDENTS   |
+-------------+
| id          |
| user_id(FK) |
| name        |
| age         |
| department  |
+-------------+
      |
      |
      v
+-------------+
|    MARKS    |
+-------------+
| id          |
| studentId   |
| subject     |
| mark        |
| grade       |
+-------------+
+-------------+
|  TEACHERS   |
+-------------+
| id          |
| name        |
| department  |
+-------------+

⸻

7. Grade Calculation Logic

Marks	Grade
90 - 100	A+
80 - 89	A
70 - 79	B+
60 - 69	B
50 - 59	C+
40 - 49	C
30 - 39	D+
Below 30	F

⸻

8. Modules

User Management

Functions:

* Add User
* View User
* Edit User
* Delete User

⸻

Teacher Management

Functions:

* Add Teacher
* View Teacher
* Edit Teacher
* Delete Teacher

⸻

Student Management

Functions:

* Add Student
* View Student
* Edit Student
* Delete Student

⸻

Mark Management

Functions:

* Add Mark
* View Mark
* Edit Mark
* Delete Mark

⸻

Login Module

The login module verifies username and password.

Admin Login

Admin can:

* Manage Users
* Manage Teachers
* Manage Students
* Manage Marks

Student Login

Student can:

* View Own Grade Report

Student cannot:

* Add Records
* Edit Records
* Delete Records
* Access Dashboard

⸻

9. Data Flow

User Login
     |
     v
Authentication
     |
     +-----> Admin
     |          |
     |          +----> User Management
     |          +----> Teacher Management
     |          +----> Student Management
     |          +----> Mark Management
     |
     +-----> Student
                |
                +----> View Own Grades

⸻

10. Advantages

* Easy to use.
* Secure login system.
* Automatic grade calculation.
* Data stored permanently in SQLite database.
* Role-based access control.
* Simple and lightweight application.

⸻

11. Limitations

* Console-based application.
* No graphical user interface.
* Passwords are stored as plain text.
* Single database file.

⸻

12. Future Enhancements

* GUI using Tkinter.
* Web Application using Flask or Django.
* Password Encryption.
* Attendance Management.
* Report Generation in PDF.
* Email Notifications.
* Dashboard with Charts.

⸻

13. Conclusion

The Student Grade System successfully manages student information and academic grades using Python and SQLite. The project demonstrates database connectivity, CRUD operations, authentication, role-based access control, and automatic grade calculation. The system provides a simple and efficient solution for maintaining student academic records.

⸻

Viva Questions and Answers

1. What is SQLite?

SQLite is a lightweight relational database management system that stores data in a single file.

2. What is CRUD?

CRUD stands for Create, Read, Update, Delete.

3. What is a Primary Key?

A Primary Key uniquely identifies each record in a table.

4. What is a Foreign Key?

A Foreign Key creates a relationship between two tables.

5. Why did you use SQLite?

SQLite is simple, lightweight, and does not require a separate server.

6. What is Authentication?

Authentication is the process of verifying a user’s identity using username and password.

7. What is Role-Based Access Control?

It is a security mechanism where users get access based on their assigned roles.

8. How are grades calculated?

Grades are calculated automatically based on the mark entered.

9. What is fetchone()?

fetchone() retrieves a single row from the query result.

10. What is fetchall()?

fetchall() retrieves all rows from the query result.
