-- Creating a table called 'Employees'
CREATE TABLE Employees (
    EmployeeID INT NOT NULL PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Age INT,
    City VARCHAR(255)
);

-- Creating an index on the LastName column
CREATE INDEX idx_lastname ON Employees (LastName);

-- Inserting data into the Employees table
INSERT INTO Employees (EmployeeID, LastName, FirstName, Age, City) VALUES
(1, 'Smith', 'John', 30, 'London'),
(2, 'Jones', 'Sarah', 25, 'Paris'),
(3, 'Williams', 'David', 40, 'New York');


-- Creating a view that shows employees older than 30
CREATE VIEW OlderEmployees AS
SELECT LastName, FirstName
FROM Employees
WHERE Age > 30;

-- Querying the view
SELECT * FROM OlderEmployees;


-- Creating a trigger that prevents updates to the Employees table on weekends
CREATE TRIGGER tr_Employees_NoUpdates ON Employees
FOR UPDATE
AS
BEGIN
    IF (DATEPART(dw, GETDATE()) IN (1, 7))  -- 1=Sunday, 7=Saturday
    BEGIN
        RAISERROR('You cannot update the Employees table on weekends.', 16, 1)
        ROLLBACK TRANSACTION
    END
END;


-- Using a cursor to loop through employees and print their names
DECLARE @EmployeeID INT, @LastName VARCHAR(255), @FirstName VARCHAR(255);

DECLARE cur_employees CURSOR FOR 
SELECT EmployeeID, LastName, FirstName FROM Employees;

OPEN cur_employees;

FETCH NEXT FROM cur_employees INTO @EmployeeID, @LastName, @FirstName;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Employee ID: ' + CAST(@EmployeeID AS VARCHAR) + ', Name: ' + @LastName + ', ' + @FirstName;

    FETCH NEXT FROM cur_employees INTO @EmployeeID, @LastName, @FirstName;
END

CLOSE cur_employees;
DEALLOCATE cur_employees;