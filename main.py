import time


print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing == "yes":
    print("Let's play then :D")
else:    
    print("Okay, maybe next time ;(")
    quit()

score = 0

print(f"You have answered {score} questions correctly so far.")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

answer = input("What does PCB stand for? ").lower()
if answer == "printed circuit board":
    print("Correct!")
    print("Good Job!")
else:
    print("Incorrect! The correct answer is printed circuit board.")
    quit()

score = 1
print(f"You have answered {score} questions correctly so far.")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

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

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

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

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

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

print("Since you scored so well on the quiz, you get to battle a friend in a quick quiz! Whoever gets the most questions right wins! ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

print("Question 1 for player 1: What is hackclubs signature colour, is it A. Blue, B. Green, C. Orange or D. Red and White ")

answer = input("Your answer: ").lower()
if answer == "d":
    print("Correct!")
    print("You know your hackclub colours!")
else: 
    print("Incorrect! The correct answer is D. Red and White.")
    print("Better luck next time!")
    print("Let's see how player 2 does!")

print("Next question")
print("In 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

print("Question 1 for player 2: What is the name of fallout's mascot? ")
answer = input("Your answer: ").lower()
if answer == "soup":
    print("Correct!")
    print("You are a hack club genius!")
else:
    print("Better luck next time! The correct answer is soup")
    print("Player 1 wins!")
    quit()

print("Congratulations! You win! You are the hack club champion! :)")
print("Now I'm bored and I have to log more hours to submit this quiz to horizons so...")

print("So now, you can create your own quiz!!!!!!!!!!!!!")

question = input ("What is your question? ").lower()
answerreal = input("What is the answer to your question? ")

print(f"Question: {question}")
answer = input("You answer: ")
if answer == answerreal:
    print("Correct!")
    print("You are a quiz master!")
else: 
    print(f"Incorrect! The correct answer is {answerreal}.")
    print("Better luck next time!")

print("Create your own quiz question again!")
print("This time, you can make it a multiple choice question by giving 4 options and asking the user to choose the correct one by typing A, B, C, or D. Like the question about the filament you got earlier in the quiz.")

question = input("What is your question? ").lower()
option = input("What are the options? ").lower()

print(f"Question: {question}")
answer = input("You answer: ").lower()
if answer == option:
    print("Correct!")
    print("You are a quiz master!")
    print("You better stop getting all these questions right or I'ma have you make more ;(")
else:
    print(f"Incorrect! The correct answer is {option}.")
    print("Better luck neext time!")
    print("I'm so tired.")

print("I hope you had fun playing this quiz! You can always play again by restarting the code! :)")
print("Goodbye!")

print("Just kidding, I have to log more hours so I can submit this quiz to horizons :)")

