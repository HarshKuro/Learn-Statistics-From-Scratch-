-- Creating a new table called 'Employees'
CREATE TABLE Employees (
    EmployeeID INT NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Age INT,
    City VARCHAR(255)
);

-- Adding a PRIMARY KEY constraint to the EmployeeID column
ALTER TABLE Employees
ADD PRIMARY KEY (EmployeeID);

-- Adding a UNIQUE constraint to the LastName column
ALTER TABLE Employees
ADD UNIQUE (LastName);

-- Adding a CHECK constraint to the Age column
ALTER TABLE Employees
ADD CHECK (Age >= 18);

-- Adding a DEFAULT constraint to the City column
ALTER TABLE Employees
ALTER COLUMN City SET DEFAULT 'Unknown';

-- Creating a new table called 'Departments'
CREATE TABLE Departments (
    DepartmentID INT NOT NULL,
    DepartmentName VARCHAR(255) NOT NULL,
    PRIMARY KEY (DepartmentID)
);

-- Adding a FOREIGN KEY constraint to the Employees table
ALTER TABLE Employees
ADD DepartmentID INT;

ALTER TABLE Employees
ADD FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID);

-- Inserting data into the Employees table
INSERT INTO Employees (EmployeeID, LastName, FirstName, Age, City, DepartmentID) VALUES
(1, 'Smith', 'John', 30, 'London', 1),
(2, 'Jones', 'Sarah', 25, 'Paris', 2),
(3, 'Williams', 'David', 40, 'New York', 1);

-- Inserting data into the Departments table
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'Sales'),
(2, 'Marketing');