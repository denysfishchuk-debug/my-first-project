SELECT Customers.CustomerID, Customers.Name, Orders.OrderID, Orders.Product, Orders.Date
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT Customers.CustomerID, Customers.Name, Orders.OrderID, Orders.Product, Orders.Date
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT Orders.OrderID, Orders.Product, Orders.Date, Customers.CustomerID, Customers.Name
FROM Orders
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

SELECT CustomerID, COUNT(OrderID)
FROM Orders
GROUP BY CustomerID;

SELECT Product, SUM(Quantity * Price) AS TotalRevenue
FROM Orders
GROUP BY Product;

CREATE INDEX idx_category ON Products(Category);

CREATE VIEW ProductsWithHighPrice AS
SELECT * FROM Products WHERE Price > 50; SELECT * FROM ProductsWithHighPrice;