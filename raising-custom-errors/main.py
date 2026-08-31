a =(input("enter a number between 1 and 10: "))
if(a == "quit"):
    print("Exiting Program")
elif (int(a)<1 or int(a)>10):
    raise ValueError("Number must be between 1 and 10")
print(f"you entered {a} successfuly")
