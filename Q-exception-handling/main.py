# Question 1 of exception handling
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try : 
    c = a/b 
    print(f"the result of the division is : {c}")
except ZeroDivisionError:
    print("division by zero is not allowed")

# Question 2 of exception handling
try:
    u = int(input("Enter your age : "))
    if u < 0:
        print("age cannot be negative")
    else:
        print(f"your age is : {u}")
except ValueError : 
    print("please enter a valid number ")
finally: 
    print("thanks for using the program")
