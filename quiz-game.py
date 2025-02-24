# Print function takes string as argument and prints it to console
print("Welcome to my computer quiz!")

# Input takes from console and store in variable but beore that use method lower() to make string lowercase
playing = input("Do you want to play? ").lower()

# If condition that quits will kick in when it evaluate to True
if playing != "yes":
    quit()
    
print("Okay! Let's play :)")
# To keep track of the score variable
score = 0 

answer = input("What does CPU stand for? ").lower()

# Question #1:
if answer == "central processing unit":
    print("Correct!")
    # Increment score by 1
    score += 1
else:
    print("Incorrect!")

# Question #2:
answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question #3:
answer = input("What does GPU stand for? ").lower()

if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question #4:
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Using fstring here to inject variable into other string
print(f"You got {score} questions correct!")
# And here you can see that fstring also allows calculations within {} brackets. Actually different expressions are allowed within the {}
print(f"Overal you are {(score * 100) / 4}% correct.")