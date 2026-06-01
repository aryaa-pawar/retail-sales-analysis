-- Top 10 Products by Revenue

SELECT
    "Product Name",
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY "Product Name"
ORDER BY Revenue DESC
LIMIT 10;


-- Highest Profit Category

SELECT
    Category,
    ROUND(SUM(Profit),2) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;


-- Monthly Sales

SELECT
    substr("Order Date",1,7) AS Month,
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;


-- Top Customers

SELECT
    "Customer Name",
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY "Customer Name"
ORDER BY Revenue DESC
LIMIT 10;


-- Regional Performance

SELECT
    Region,
    ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;


-- Loss Making Products

SELECT
    "Product Name",
    ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY "Product Name"
ORDER BY Profit ASC
LIMIT 10;