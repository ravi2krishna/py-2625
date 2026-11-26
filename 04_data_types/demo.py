# Data Types

# Numeric Types 

data = 10 
print(type(data))

data = 10.5 
print(type(data))

# complex number -> a + ib
# data = 3 + i5 
# print(type(data))

# complex number -> a + bj
data = 3 + 5j 
print(type(data))

data = True
print(type(data))

data = False
print(type(data))

data = None
print(type(data))

data = "python"
print(type(data))


# Complex Data Types 

# List
data = [10,20,30,40,50]
print(type(data))

# Tuple
data = (10,20,30,40,50)
print(type(data))

# Set
data = {10,20,30,40,50}
print(type(data))

# Dictionary
# {key1:value1, key2:value2, key3:value3} # Properties
data = {"course":"python","time":11,"duration":1.5}
print(type(data))

# Custom Data Type Requirement From Training Institute To Store Students Data 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    student_contact = 99009090900
    student_gpa = 9.3
    student_enrolled_courses = ["python","sql","ai"]
    
data = Student()
print(type(data))

# Type Conversion / Implicit Conversion [Automatic]
n1 = 10 # int
n2 = 5.5 # float 
sum = n1 + n2 # float 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1120.50 # float 
print(price)
print(type(price))

# round off price and put in int format
round_off_price = price
print(round_off_price)
print(type(round_off_price))

round_off_price = int(price) # Type Casting
print(round_off_price)
print(type(round_off_price))

