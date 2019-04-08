-- Drop table INSTRUCTOR in case it already exists
DROP TABLE INSTRUCTOR;

-- Create table INSTRUCTOR
CREATE TABLE INSTRUCTOR(
	ins_id INTEGER PRIMARY KEY NOT NULL,
	lastname VARCHAR(15) NOT NULL,
	firstname VARCHAR(15) NOT NULL,
	city VARCHAR(15),
	country CHAR(2)
);

-- Insert single row for Rav Ahuja
INSERT INTO INSTRUCTOR
	(ins_id, lastname, firstname, city, country)
	VALUES
	(1, 'Ahuja', 'Rav', 'Toronto', 'CA')
;

-- Insert the two rows for Raul and Hima
INSERT INTO INSTRUCTOR
  VALUES
  (2, 'Chong', 'Raul', 'Toronto', 'CA'),
  (3, 'Vasudevan', 'Hima', 'Chicago', 'US')
;

-- Select all rows in the table
SELECT * FROM INSTRUCTOR;

-- Select firstname, lastname and country where city is Toronto
SELECT firstname, lastname, country 
	FROM INSTRUCTOR 
	WHERE city='Toronto'
;

-- Change the city for Rav to Markham
UPDATE INSTRUCTOR 
	SET city='Markham' 
	WHERE ins_id=1
;

-- Delete the row for Raul Chong
DELETE FROM INSTRUCTOR 
	WHERE ins_id=2
;

-- Retrieve all rows from the table
SELECT * FROM INSTRUCTOR;
