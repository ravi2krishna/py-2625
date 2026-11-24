# Variables

# Assign Data (Store Data)
student_name = "Ravi" # string
student_age = 20 # int 
student_gpa = 9.3 # float

student_passed = True # Correct (Student Has Passed)
student_failed = False # Incorrect (Student Din't Fail)
# STUDENT_AADHAR_ID # NameError: name 'STUDENT_AADHAR_ID' is not defined
STUDENT_AADHAR_ID = None # Absence Of Value


# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_failed)
print(STUDENT_AADHAR_ID)

# Concatenation: Join Strings Using + Operator
print("=============== Student Information ===============")

print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age)
print("Student GPA: ", student_gpa)
print("Did Student Passed: ", student_passed)
print("Did Student Failed: ", student_failed)
print("Student AADHAR ID: ", STUDENT_AADHAR_ID)

print("=============== Student Information ===============")

# type() function Used To Tell Data Type 
print(type(student_name)) # student_name is an object of String Class 
print(type(student_age)) # student_age is an object of int Class 
print(type(student_gpa)) 
print(type(student_passed))
print(type(student_failed))
print(type(STUDENT_AADHAR_ID))

print("==============================")

# id() function Used To Get Memory Address 
print(id(student_name))
print(id(student_age)) 
print(id(student_gpa)) 
print(id(student_passed))
print(id(student_failed))
print(id(STUDENT_AADHAR_ID))

print("==============================")

# Memory Model In Python 
value_x = 10
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10
print(id(value_z))

student_name = "Ravi" 
print(id(student_name))
trainer_name = "Ravi" 
print(id(trainer_name))

