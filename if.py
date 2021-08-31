
answer = input("Do you want to hear a joke? ")

if answer == "Yes":
    print("I'm against picketing, but I don't know how to slow it.")
   

In if.py: 

answer = input("Do you want to hear a joke? ")

if answer == "Yes" or answer == "yes":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
elif answer == "No" or answer == "no" :
    print("Fine.")
else:
    print("I don't understand.")
     
    
    answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")
    
    
    
answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")
    
    
    
#And we can use .lower to eliminate the need for a list entirely: 
    
answer = input("Do you want to hear a joke? ")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if answer.lower() in affirmative_responses:
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")
