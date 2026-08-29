def fibonacci(n):
    if n == 0 :
        return 0 
    elif n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
a = int(input("Enter the the vale of n : "))
print(f"The {a}th term of the Fibonacci series is : {fibonacci(a)}")
