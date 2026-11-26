# Arithmetic Operators 

num1 = 10
num2 = 5

print("Sum Of Number: ", num1 + num2)
print("Difference Of Number: ", num1 - num2)
print("Product Of Number: ", num1 * num2)
print("Division Of Number: ", num1 / num2)
print("Modulus Of Number: ", num1 % num2)

print("Division Of Number: ", num1 / num2)
print("Floor Division Of Number: ", num1 // num2)

print("Exponentiation Of Number: ", num1 ** num2) # num1 ^ num2 

print("Exponentiation Of Number: ", 3 ** 2) # 3 ^ 2 

print("==============================")

# Compound Assignment Operators 
num = 10
num = num * 5 # long form
print(num) 

num = 10
num *= 5 # short form
print(num) 

# Increment
count = 1
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)

# Decrement
count = 10
print(count)
count -= 1
print(count)
count -= 1
print(count)
count -= 1
print(count)

print("==============================")

# Comparison Operators 

num1 = 3
num2 = 5 
num3 = 3

print(num1 > num2) 
print(num1 == num3) 
print(num1 != num3)
print(num2 > num1) 

print("==============================")

# Logical Operators 

num1 = 1
num2 = 2 
num3 = 3
num4 = 4 

print(num1 < num2 and num3 < num4) # T and T = T
print(num1 > num2 and num3 < num4) # F and T = F

print(num1 > num2 or num3 < num4) # F or T = T
print(num1 > num2 or num3 > num4) # F or F = F

print(num1 > num2) # F 
print(not num1 > num2) # F -> T

print("==============================")

# Membership Operators 
data = "python is an programming language"
find_word = "hello"
match_status = find_word in data
print("Found Word: ",match_status)

print("==============================")

data = "python is an programming language"
find_word = "python"
match_status = find_word in data
print("Found Word: ",match_status)

print("==============================")

# List Data Type -> List Stores Multiple Values in []
list_of_products = ["mobile","keyboard","laptop","earphone","pc","laptop"]
find_product = "shoe"
match_status = find_product in list_of_products
print("Product Found: ",match_status)

print("==============================")

list_of_products = ["mobile","keyboard","laptop","earphone","pc","laptop"]
find_product = "laptop"
match_status = find_product in list_of_products
print("Product Found: ",match_status)

print("==============================")

list_of_products = ["mobile","keyboard","laptop","earphone","pc","laptop"]
find_product = "shoe"
match_status = find_product not in list_of_products 
print("Shoe Not Found: ",match_status)

print("==============================")

# Identity Operators 

value_x = 10
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10
print(id(value_z))

print(value_x is value_y) # False 

print(value_x is value_z) # True 

print(value_x is not value_y) # True 

print("==============================")

# Bitwise Operators 

n1 = 5 # 0000 0101
n2 = 3 # 0000 0011
print(n1 | n2) # 7
print(n1 & n2) # 1 - 

print("==============================")