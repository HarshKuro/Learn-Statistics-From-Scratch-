-- Creating the Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    ContactName VARCHAR(255),
    Country VARCHAR(255)
);

-- Creating the Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Inserting data into the Customers table
INSERT INTO Customers (CustomerID, CustomerName, ContactName, Country) VALUES
    (1, 'Alfreds Futterkiste', 'Maria Anders', 'Germany'),
    (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Mexico'),
    (3, 'Antonio Moreno Taquería', 'Antonio Moreno', 'Mexico'),
    (4, 'Around the Horn', 'Thomas Hardy', 'UK');

-- Inserting data into the Orders table
INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES
    (10308, 2, '1996-09-18'),
    (10365, 3, '1996-11-27'),
    (10383, 4, '1996-12-16'),
    (10355, 4, '1996-11-15'),
    (10278, 1, '1996-08-12');

-- INNER JOIN: Retrieve all orders with customer information
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- LEFT JOIN: Retrieve all customers and their orders (if any)
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

-- RIGHT JOIN: Retrieve all orders and their corresponding customers (if any)
SELECT Orders.OrderID, Customers.CustomerName
FROM Customers
RIGHT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Orders.OrderID;