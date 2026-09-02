# making a secret code langauge by adding 3 random letters at the start and end of the word and moving the first letter to the end of the word
import random
alphabets = "abcdefghijklmnopqrstuvwxyz"
choice = input("Enter 'C' for Coding or 'D' for Decoding : ").strip().lower()
message = input("enter the message : ")
words = message.split()
# Coding the message by adding 3 random letters at the start and end of the word and moving the first letter to the end of the word
if (choice == "c"):
    coding = True
    result = []
    for word in words:
        if (len(word) >= 3):
          new_word = random.choice(alphabets) + random.choice(alphabets) + random.choice(alphabets)
          new_word += word[1:] + word[0]
          new_word += random.choice(alphabets) + random.choice(alphabets) + random.choice(alphabets)
          result.append(new_word)
        else:
            result.append(word[: : -1])
    print("The coded message is : ", " ".join(result))
# Decoding the message by removing the first 3 and last 3 letters and moving the last letter to the start of the word
elif (choice == "d"):
    coding = False
    result = []
    for word in words:
        if (len(word) >= 3):
            new_word = word[3:-3]
            new_word = new_word[-1] + new_word[:-1]
            result.append(new_word)
        else: 
            result.append(word[: : -1])
    print("The decoded message is : ", " ".join(result))
else:
    print("Invalid choice. Please enter 'C' for Coding or 'D' for Decoding.")