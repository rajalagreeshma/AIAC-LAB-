--Task 1 – Hospital Management Database
--Task:Create schema and queries for a Hospital Management System.
--Instructions:
--•Tables: Doctors, Patients, Appointments.
--•Use AI to define constraints (unique IDs, valid dates).
--•Generate queries:
--•List all appointments for a specific doctor.
--•Retrieve patient history by patient ID.
--•Count total patients treated by each doctor.
--Expected Output:Normalized schema and SQL queries with joins.
--Create Doctors table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) NOT NULL
);
--Create Patients table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL
);
--Create Appointments table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
--Insert sample data into Doctors table
INSERT INTO Doctors (doctor_id, name, specialty) VALUES
(1, 'Dr. Smith', 'Cardiology'),
(2, 'Dr. Johnson', 'Neurology');
--Insert sample data into Patients table
INSERT INTO Patients (patient_id, name, date_of_birth) VALUES
(1, 'Alice Brown', '1980-05-15'),
(2, 'Bob Green', '1990-08-22');
--Insert sample data into Appointments table
INSERT INTO Appointments (appointment_id, doctor_id, patient_id, appointment_date) VALUES
(1, 1, 1, '2024-07-01'),
(2, 1, 2, '2024-07-02'),
(3, 2, 1, '2024-07-03');
--Query: List all appointments for a specific doctor (e.g., Dr. Smith)
SELECT a.appointment_id, p.name AS patient_name, a.appointment_date
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = 1;
--Query: Retrieve patient history by patient ID (e.g., patient_id = 1)
SELECT a.appointment_id, d.name AS doctor_name, a.appointment_date
FROM Appointments a
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1;
--Query: Count total patients treated by each doctor
SELECT d.name AS doctor_name, COUNT(DISTINCT a.patient_id) AS total_patients
FROM Doctors d
LEFT JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.name;

SELECT * FROM Doctors;
SELECT * FROM Patients;
SELECT * FROM Appointments;


--Task 2 – Real-Time Application: Online Shopping Database
--Scenario:Design a database for an E-commerce platform.
--Requirements:
--• Tables: Users, Products, Orders, OrderDetails.
--• Generate queries to:
--• Retrieve all orders by a user.
--• Find the most purchased product.
--• Calculate total revenue in a given month.
--• AI should also suggest normalization improvements and query optimization.
--Expected Output: Complete schema with relationships + SQL queries for analytics

-- Users Table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    registered_date DATE NOT NULL
);

-- Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- OrderDetails Table
CREATE TABLE OrderDetail (
    order_detail_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
--Retrieve all orders by a user
SELECT o.order_id, o.order_date, o.status,
       p.name AS product_name, od.quantity, p.price
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE o.user_id = 301;  -- Replace 301 with the user’s ID

--Find the most purchased product
SELECT p.product_id, p.name AS product_name,
       SUM(od.quantity) AS total_quantity
FROM OrderDetail od
JOIN Products p ON od.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY total_quantity DESC
LIMIT 1;

--Calculate total revenue in a given month
SELECT strftime('%m', o.order_date) AS month,
       strftime('%Y', o.order_date) AS year,
       SUM(od.quantity * p.price) AS total_revenue
FROM Orders o
JOIN OrderDetail od ON o.order_id = od.order_id
JOIN Products p ON od.product_id = p.product_id
WHERE strftime('%m', o.order_date) = '03'
  AND strftime('%Y', o.order_date) = '2026'
GROUP BY strftime('%m', o.order_date), strftime('%Y', o.order_date);

SELECT * FROM USERS;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM OrderDetail;





--Task 3 – Library Database
--Task:Design schema for a Library Management System.
--Instructions:
--•Tables: Books, Members, Loans.
--•Use AI to suggest indexing strategy for faster queries.
--•Generate queries:
--•Retrieve all books currently issued.
--•Find overdue books (loan date > 30 days).
--•Count number of books loaned by each member.
--Expected Output:Schema + SQL queries demonstrating joins and conditions.

-- Books Table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    published_year INT
);

-- Members Table
CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) UNIQUE,
    membership_date DATE NOT NULL
);

-- Loans Table
CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    CONSTRAINT chk_loan_date CHECK (loan_date >= '2000-01-01')
);

-- Retrieve all books currently issued (not yet returned)
SELECT b.book_id, b.title, b.author, m.name AS member_name, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;


--Find overdue books (loan date > 30 days and not returned)
SELECT b.book_id, b.title, m.name AS member_name, l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL
  AND l.loan_date <= DATE('now','-30 days');

SELECT * FROM Loans 
JOIN Books b ON l.book_id = b.book_id
JOIN Members m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;


--Task 4: Optimize Queries
--Instructions:
--• Use AI tools to analyze query efficiency.
--• Optimize inefficient queries using joins, indexes, or reducing subqueries.
--• Test optimized queries for correctness.
--Starter Code Example:
-- Original query
--SELECT * FROM Books WHERE author_id IN (SELECT author_id FROM
--Authors WHERE country='UK');
-- Optimized query
--SELECT b.*
--FROM Books b
--JOIN Authors a ON b.author_id = a.author_id
--WHERE a.country = 'UK';
--Expected Output:
--• Both queries return the same result: all books written by UK authors.
--• Optimized query performs faster for larger datasets.
-- Original query to find all books by UK authors

SELECT b.*
FROM Books b
JOIN Authors a 
ON b.author_id = a.author_id
WHERE a.country = 'UK';
CREATE INDEX idx_author_id ON Books(author_id);
CREATE INDEX idx_country ON Authors(country);
-- Check difference (should return 0 rows)
SELECT * FROM (
    SELECT * FROM Books 
    WHERE author_id IN (
        SELECT author_id FROM Authors WHERE country = 'UK'
    )
) AS q1
EXCEPT
SELECT b.*
FROM Books b
JOIN Authors a 
ON b.author_id = a.author_id
WHERE a.country = 'UK';






--Task 5: University Course Registration
--Scenario:SR University needs a course registration system for students enrolling in different courses under faculty supervision.
-- Use Copilot to design schema tables: Students, Courses, Faculty, and Registrations.
--• Define relationships:
--• Each student can register for multiple courses.
--• Each course is taught by a faculty member.
--• Write SQL queries to:
--• List all students enrolled in a specific course.
--• Find faculty members teaching more than 2 courses.
--• Retrieve courses with the highest number of registrations.


--Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50)
);

--Faculty Table
CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);

--Courses Table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    faculty_id INT,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
);

--Registrations Table (Many-to-Many Relationship)
CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    registration_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

--List all students enrolled in a specific course
SELECT s.student_id, s.name, s.email
FROM Students s
JOIN Registrations r ON s.student_id = r.student_id
JOIN Courses c ON r.course_id = c.course_id
WHERE c.course_name = 'Database Systems';

--Find faculty members teaching more than 2 courses
SELECT f.faculty_id, f.name, COUNT(c.course_id) AS total_courses
FROM Faculty f
JOIN Courses c ON f.faculty_id = c.faculty_id
GROUP BY f.faculty_id, f.name
HAVING COUNT(c.course_id) > 2;

--Retrieve courses with the highest number of registrations
SELECT c.course_id, c.course_name, COUNT(r.student_id) AS total_students
FROM Courses c
JOIN Registrations r ON c.course_id = r.course_id
GROUP BY c.course_id, c.course_name
HAVING COUNT(r.student_id) = (
    SELECT MAX(course_count)
    FROM (
        SELECT COUNT(student_id) AS course_count
        FROM Registrations
        GROUP BY course_id
    ) AS temp
);
