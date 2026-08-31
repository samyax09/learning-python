questions = ["What is the Capital of India?", "Who is Prime Minister of India?", "Who invented Zero?", "Who is the Father of Nation?", "What is the currency of India?", "How many states are there in India?"]
options = [
    ["New Delhi", "Mumbai", "Kolkata", "Burari"],
    ["Narendra Modi", "Manmohan Singh", "Samyax", "Jawaharlal Nehru"],
    ["Aryabhatta", "Galileo", "Einstein", "Newton"],
    ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Bal Gangadhar Tilak"],
    ["Indian Rupee", "US Dollar", "Euro", "British Pound"],
    ["28", "29", "30", "31"]
]
answers = ["New Delhi", "Narendra Modi", "Aryabhatta", "Mahatma Gandhi", "Indian Rupee", "28"]
name = input("Enter your Name : ")
print(f"Hello {name} , WELCOME TO KBC (KAUN BANEGA CROREPATI)!!!")
score = 0 
for i ,(question , option , c_answer) in enumerate(zip(questions , options , answers) , start = 1):
    print(f"Q{i}. {question}")
    print("Options: " , option)
    ans = input("Enter your Answer :")
    if ans.strip().lower() == c_answer.lower():
        print("Correct Answer")
        score +=1
    else:
        print("Wrong Answer")
print(f"Your Final Score is : {score}")
if score == 6:
    print("AAP JEET TE HAI 1 CROREEEEE")
elif score == 5 or score == 4:
    print("AAP JEET TE HAI HAZAAR RUPAYEE")
elif score == 3 or score == 2:
    print("AAP JEET TE HAI 100 RUPAYEE")
elif score == 1 or score == 0:
    print("AAP JEET TE HAI KUCH BHI NAHI")
    
