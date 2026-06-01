import sqlite3
import pandas as pd

conn = sqlite3.connect("sql/superstore.db")

print("\nTOP 10 PRODUCTS BY REVENUE\n")

query1 = """
SELECT
    "Product Name",
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY "Product Name"
ORDER BY Revenue DESC
LIMIT 10;
"""

print(pd.read_sql(query1, conn))

print("\nHIGHEST PROFIT CATEGORY\n")

query2 = """
SELECT
    Category,
    ROUND(SUM(Profit),2) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;
"""

print(pd.read_sql(query2, conn))

print("\nMONTHLY SALES\n")

query3 = """
SELECT
    substr("Order Date",1,7) AS Month,
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
"""

print(pd.read_sql(query3, conn))

print("\nTOP 10 CUSTOMERS\n")

query4 = """
SELECT
    "Customer Name",
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY "Customer Name"
ORDER BY Revenue DESC
LIMIT 10;
"""

print(pd.read_sql(query4, conn))

print("\nREGIONAL PERFORMANCE\n")

query5 = """
SELECT
    Region,
    ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;
"""

print(pd.read_sql(query5, conn))

print("\nLOSS MAKING PRODUCTS\n")

query6 = """
SELECT
    "Product Name",
    ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY "Product Name"
ORDER BY Profit ASC
LIMIT 10;
"""

print(pd.read_sql(query6, conn))

conn.close()