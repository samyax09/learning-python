import random
user = input("Enter your name : ").capitalize()
print(f"welcome {user} to rock , paper and scissors")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input(" Enter rock , paper or scissors : ").lower()
print("Computer : " ,computer_choice)
 
 # Tie situation 
if user_choice == computer_choice:
    print("Tie")
# User winning situation 
elif user_choice == "rock" and computer_choice == "scissors":
    print(f"{user} won")
elif user_choice == "scissors" and computer_choice == "paper":
    print(f"{user} won")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"{user} won")
# User loosing situation 
elif user_choice == "scissors" and computer_choice == "rock":
    print("computer won")
elif user_choice == "rock" and computer_choice == "paper":
    print("computer won")
elif user_choice == "paper" and computer_choice == "scissors":
    print("computer won")
else:
    print("invalid enter only rock , paper and scissors")
print(f"THANKS {user} FOR PLAYING THE GAME")    