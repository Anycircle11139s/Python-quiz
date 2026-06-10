print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing == "yes":
    print("Let's play then :D")
else:    
    print("Okay, maybe next time ;(")
    quit()

score = 0

print(f"You have answered {score} questions correctly so far.")

answer = input("What does PCB stand for? ").lower()
if answer == "printed circuit board":
    print("Correct!")
    print("Good Job!")
else:
    print("Incorrect! The correct answer is printed circuit board.")
    quit()

score = 1
print(f"You have answered {score} questions correctly so far.")

answer = input("What is the most popular programming language? ").lower()
if answer == "python":
    print("Correct!")
    print("Your acing this!")
else:
    print("Incorrect! The correct answer is python.")
    print("Better luck next time!")
    quit()

score = 2
print(f"You have answered {score} questions correctly so far.")

answer = input("What is the most common filament used in 3D printing?"
"Is it A.ABS, B.PLA, C.PETG or D.TPU? ").lower()
if answer == "b":
    print("Correct!")
    print("How did you know that?!")
else:
    print("Incorrect! The correct answer is B.PLA")
    print("Better luck next time!")
    quit()

score = 3
print(f"You have answered {score} questions correctly so far.")

answer = input("What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct!")
    print("You know your stuff!")
else: 
    print("Incorrect!")
    print("The correct answer is hypertext markup language.")
    quit()

score = 4
print(f"You have answered {score} questions correctly so far.")

print("Congratulations! You have completed the quiz!")
print("You beat everyone else who failed this quiz! You can choose to try again by restarting the code, or you can just be proud of yourself for being so smart! :)")
