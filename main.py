a = input("enter any number: ")
try: 
    for i in range(1,11):
        print(f"{a} X {i} = {(int(a)*i)}")
except:
    print("error occured due to invalid input")
    print("please enter a number only!!")
finally:
    print("thank you for using the program")
    