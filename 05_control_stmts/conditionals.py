# Conditional Structures (Decision Making Statements) 

# if 

if 5 > 2:
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")

print("========================")

if False: # Code is not analyzed because condition is statically evaluated as false
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")

print("========================")

if 0 > 2:
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")

print("========================")

num = 5 # positive 

if num > 0:
    print("Given Num Is Positive")

print("========================")

num = -5

if num > 0:
    print("Given Num Is Positive")
if num < 0:
    print("Given Num Is Negative")
    
print("========================")

# if else 
num = 15
if num > 0:
    print("Given Num Is Positive")
else:
    print("Given Num Is Negative")
    
print("========================")

# input() For Taking Input From User 
# full_name = "Ravi Krishna"
full_name = input("Enter Your Full Name: ")
print("Hi: ",full_name)
# email = input("Enter Your Email: ")
# print("You Joined With Email: ",email)
# zip_code = input("Enter Your Postal Code: ")
# print("Your Current Postal Address Is: ",zip_code)

print("========================")

num = input("Enter Number: ")
# if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
num = int(num)
if num > 0:
    print("Given Num Is Positive")
else:
    print("Given Num Is Negative")
    
print("========================")

num = input("Enter Number: ")
# if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
num = int(num)
if num > 0:
    print(f"Given Num {num} Is Positive")
else:
    print(f"Given Num {num} Is Negative")
    
print("========================")

# without interpolation
full_name = input("Enter Your Full Name: ")
email = input("Enter Your Email: ")
print("Welcome " + full_name + " Your Login Email is " + email)

print("========================")

# with interpolation
full_name = input("Enter Your Full Name: ")
email = input("Enter Your Email: ")
print(f"Welcome {full_name} Your Login Email is {email}")

print("========================")

# Voting Application 
full_name = input("Enter Your Full Name: ")
age = int(input("Enter Your Age: "))
if age >= 18:
    print(f"{full_name} Can Vote")
else:
    print(f"{full_name} You Cannot Vote, You Are Just {age}")
    
print("========================")

# Conditional Expression 
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age: "))
print(f"You Can Vote" if age >= 18 else f"You Cannot Vote, You Are Just {age}" )
