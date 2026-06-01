import sqlite3
import pandas as pd

conn = sqlite3.connect("sql/superstore.db")

query = """
SELECT Category,
       ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()