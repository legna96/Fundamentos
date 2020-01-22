/*operaciones inciales*/
SHOW databases;
use sql_curso_freecodecamp;

/*Operaciones tabla*/
SHOW TABLES;

CREATE TABLE IF NOT EXISTS student(
	student_id INTEGER AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL,
	major VARCHAR(20) NOT NULL,
	PRIMARY KEY (student_id)
)

DESCRIBE student;
ALTER TABLE student ADD COLUMN gpi DECIMAL(3,2) NOT NULL DEFAULT 3.14;
ALTER TABLE student DROP COLUMN gpi;
TRUNCATE TABLE student;
DROP TABLE student;

/*Operaciones Crud*/
INSERT INTO student (name, major) VALUES ("Mike", "Comp. Sci");

SELECT * FROM student;

UPDATE student
SET major = "Graphics Design", name = "Terry"
WHERE student_id = 4;

DELETE FROM student
WHERE major = "Computer Science";




