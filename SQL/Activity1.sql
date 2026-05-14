CREATE TABLE myStudents(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    grade VARCHAR(10),
    marks DECIMAL(5, 2)
);


INSERT INTO myStudents (id, name, grade, marks) VALUES (1, 'Mark', 'A', 95.50);
INSERT INTO myStudents (id, name, grade, marks) VALUES (2, 'Bob', 'B', 85.00);
INSERT INTO myStudents (id, name, grade, marks) VALUES (3, 'Bobby', 'A', 92.75);
INSERT INTO myStudents (id, name, grade, marks) VALUES (4, 'Davidd', 'C', 78.00);
INSERT INTO myStudents (id, name, grade, marks) VALUES (5, 'Eve', 'B', 88.25);

SELECT name, marks FROM myStudents WHERE grade='A';