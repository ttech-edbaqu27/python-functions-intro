# 1 - Function Declaration
def myFunction():
    print("My function is working!")

myFunction() # Output: My function is working!

# ========================================

# 2 - Parameters
def add_numbers(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1+num2}")

add_numbers(16, 9) # Output: The sum of 16 and 9 is 25

# ========================================

# 3 - Returning
def exponentiation(num, pow):
    return num ** pow

result = exponentiation(2, 6) # this now equals 64
print(result) # 64