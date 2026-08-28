l1 = ["What is the Capital of India ", "Who is Prime Minister of India ", "Who invented Zero " , "Who is the Father of Nation " , "What is the currency of India", "How many states are there in India "]
l2 = ["Delhi", "Narendra Modi", "Aryabhatta", "Mahatma Gandhi" , "Rupee", "28"]
a = input("Enter your name: ")
print("Hello" , a , "Welcome To KBC(KAUN BANEGA CROREPATI)!!!")
score = 0 
for i in range(5):
    if i == 0:
        print("Q1.", l1[0])
        print("Options: Delhi , Mumbai , Chennai , Kolkata ")
        i = input("Enter Your Answer : ")
        if i == l2[0]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        print("Q2.", l1[1])
        print("Options: Narendra Modi , Rahul Gandhi , Meee , Samyax Dixit")
        i = input("Enter your Answer : ")
        if i == l2[1]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        print("Q3.", l1[2])
        print("Options: Aryabhatta , Galileo , Newton , Einstein")
        i = input("Enter your Answer : ")
        if i == l2[2]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        print("Q4.", l1[3])
        print("Options: Mahatma Gandhi , Samyax Dixit , Jawaharlal Nehru , Subhas Chandra Bose")
        i = input("Enter your Answer : ")
        if i == l2[3]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        print("Q5.", l1[4])
        print("Options: Rupee , Dollar , Euro , Yen")
        i = input(" Enter your Answer : ")
        if i == l2[4]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        print("Q6.", l1[5])
        print("Options: 28 , 29 , 30 , 31")
        i = input("Enter your Answer : ")
        if i == l2[5]:
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
print("Your final score is:", score)
if score == 6:
    print("AAP JEET TE HAI 1 CROREEEEE")
elif score == 5 or score == 4:
    print("AAP JEET TE HAI HAZAAR RUPAYEE")
elif score == 3:
    print("AAP JEET TE HAI SO RUPAYEE")
else :
    print("AAP JEET TE HAI KUCH BHI NAHI")
