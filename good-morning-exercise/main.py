import time
time = int(time.strftime('%H'))
print(time)
if time >=0 and time<=12 :
  print("Good Morning")
elif time>12 and time<18 :
  print("Good Afternoon")
else :
  print("Good Night")