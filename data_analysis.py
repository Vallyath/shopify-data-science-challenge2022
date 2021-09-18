import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
This python script is how I went about calculating, I also have written a little about my thought process below!
The PDF contains my answers in full though!

Feel free to run this code though! I have attached my virtual env requirements.txt so you can run the command: pip install -r requirements.txt
Although, most of the outputs have been attached already.
'''


#takes in the excel sheet as a whole
df = pd.read_excel('data-science-challenge.xlsx', sheet_name='Sheet1')

#plots out the data, so we can see some outliers
"""plt.boxplot(x=df.order_amount)
plt.savefig("boxplot_initial.jpg")
"""
print("Price before the changes: ", np.sum(df.order_amount))
print("Average Shoe Value: ", (np.sum(df.order_amount)/np.sum(df.total_items)))

'''
Removes the outliers, since with the boxplot we determined that values above >= 10000 are 
inflating the price. We can remove them.
'''
"""df = df.drop(df[df.order_amount >= 10000].index)
plt.boxplot(x=df.order_amount)
plt.savefig("boxplot_1st_run.jpg")"""

#this is a 2nd run through of the data after reviewing the first runthrough, the box plot still
#had outliers that could've affect our AOV calculation.
df = df.drop(df[df.order_amount > 700].index)
plt.boxplot(x=df.order_amount)
plt.savefig("boxplot_2nd_run.jpg")

#Recalculating the values used in the AOV.
order_value = np.sum(df.order_amount)
total_orders = len(df.order_amount)

print("Price after the changes: ", order_value)
print("Total # of orders after the changes: ", total_orders)
print("AOV after the changes: ", order_value/total_orders)


'''
ANSWERS TO PART 2 (also in the pdf):

1.) 54 orders, 
Query used: 
SELECT COUNT(*) FROM [Orders] 
LEFT JOIN [Shippers]
ON [Orders].ShipperID = [Shippers].ShipperID
WHERE LOWER(ShipperName) LIKE '%speedy express%'

2.) The last name is Peacock, 
Query used:
SELECT Orders.EmployeeID, COUNT(*) AS NUM_OF_ORDERS, LastName
FROM [Orders] AS Orders
LEFT JOIN [Employees] AS Employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY NUM_OF_ORDERS DESC

3.) The product ordered the most by people in Germany is Boston Crab Meat.
Query used:
SELECT 
Country,
PRODUCTS.ProductID,
SUM(Quantity) AS TOTAL_QUANTITY,
ProductName
FROM [Orders] AS ORDERS
LEFT JOIN [Customers] AS CUSTOMERS
ON ORDERS.CustomerID = CUSTOMERS.CustomerID
LEFT JOIN [OrderDetails] AS DETAILS
ON ORDERS.OrderID = DETAILS.OrderID
LEFT JOIN [Products] AS PRODUCTS
ON DETAILS.ProductID = PRODUCTS.ProductID 
WHERE LOWER(CUSTOMERS.Country) LIKE '%germany%'
GROUP BY COUNTRY, PRODUCTS.ProductID, ProductName
ORDER BY TOTAL_QUANTITY DESC

'''

