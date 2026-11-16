#Python workshop participants are {101, 102, 103, 104, 105}, and
#Data Science workshop participants are {103, 104, 105, 106, 107}.
#Perform the following tasks:
#Create two sets for both workshops.
python = {101, 102, 103, 104, 105}
Data_Science = {103, 104, 105, 106, 107}
#Display all unique students registered for either workshop.
uniqeu_students = python.union(Data_Science)
print(uniqeu_students)
output:{101, 102, 103, 104, 105, 106, 107}
#Identify students registered for both workshops.
both_students = python.intersection(Data_Science)
print(both_students)
output:{103, 104, 105}
#Identify students registered only for the Python workshop.
only_python = python.difference(Data_science)
print(only_python)
output:{102, 102}
#Identify students registered only for the Data Science workshop.
only_data_science = Data_Science.difference(python)
print(only_data_science)
output:{106, 107}
#Q3. Online Shopping – Product Availability
#Set methods: update(), intersection(), difference()
#Scenario: An online shopping website maintains two sets of product IDs.
#Products currently available in the warehouse are {201, 202, 203, 204, 205}, and
#products requested by customers are {202, 204, 205, 206, 207}.
#Perform the following tasks:
#Create two sets representing available and requested products.
product_current_available = {201, 202, 203, 204, 205}
product_requested = {202, 204, 205, 206, 207}
#Add two newly arrived products, 208 and 209, to the warehouse.
product_current_available = {201, 202, 203, 204, 205}
product_requested = {202, 204, 205, 206, 207}
product_current_available.update([208, 209])
print(product_current_available)
product_requested.update([208,209])
print(product_requested)
output:product_current_available = {201, 202, 203, 204, 205, 208, 209}
product_requested = {202, 204, 205, 206, 207, 208, 209}
#Identify products that can be delivered to customers.
#Identify products requested by customers but currently unavailable.
#Display the updated warehouse product list.
