SELECT name, major FROM student

WHERE major IN ('Comp sci', 'Biology') OR name LIKE 'K%' ORDER BY name ;


UPDATE student
SET major = 'Comp sci'
WHERE student_id = 3;


INSERT into student VALUES (4, 'Tom', 'Biochemistry');
