# Asking user for input
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

# For Addition and Subtraction
sum_result = num1 + num2
diff_result = num1 - num2

print("Addition result is: ", sum_result)
print("Subtraction result is: ", diff_result)

# For Multiplication of two inputs
product = num1 * num2
print("Multiplication of two input is: ", product)

# For Division of two inputs
if num2 != 0:
    division = num1 / num2
    print("Division of two numbers is:", division)
else:
    print("Division: Cannot divide by zero")
