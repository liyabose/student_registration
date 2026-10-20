CREATE DATABASE student_registration;

USE student_registration;

CREATE TABLE students
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    age INT NOT NULL,

    course VARCHAR(100) NOT NULL
);