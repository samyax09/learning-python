for i in range(12):
    if(i==10):
        print("End of table")
        continue
     
    print("5 X",i+1,"=", 5*(i+1))
n = 1
while True:
    print(n)
    n=n+1
    if(n%15==0):
        break