import random
print("====================== Guess the number game ===============================")
number=random.randint(5,10)
print("Guess a number b/w 5 and 10")
attempts=0
max_attempts=3
while attempts<max_attempts:
    input_user = int(input("Guess the number: "))
    if input_user==number:
        print("Your guess it right :)")
        break
    elif input_user>number:
        print("try lower number ")
    else:
        print("try higher number ")

    attempts +=1
    if attempts==max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {number}. Better luck next time!")

