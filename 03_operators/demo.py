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

