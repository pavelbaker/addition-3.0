import random

def quiz(questions, difficulty):
    score= 0
    difficulty = difficulty.lower()
    
    for j in range(questions):

        if difficulty == "easy":
            a = random.randint(0,10)
            b = random.randint(0,10)
    
        elif difficulty == "medium":
            a = random.randint(0,100)
            b = random.randint(0,100)
        elif difficulty == "hard":
            a = random.randint(0,1000)
            b = random.randint(0,1000)
        else:
            print("This is not a recognised difficuly. Please choose either 'easy', 'medium' or 'hard'.")
            return

        answer = a+b

        while True:
            try:
                user_answer = input(f"What is {a} + {b}? ")
                if answer == int(user_answer):
                    print("You are correct")
                    score+=1
                    break
                else:
                    print("Incorrect")
                    break
            except ValueError:
                print("This is not a number, try again")

    print(f"You got {score} out of {questions}")
