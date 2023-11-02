import random

num1=random.randint(1,10)

num2=random.randint(1,10)

opr=random.choice(["+","-","*","/"])

RES=print(f"Tell me the answer {num1} {opr} {num2} ")
user=int(input("Enter your answer "))
if opr=="+":
    res=num1+num2
    if user==res:
        print("Your are correct !")
    else:
        print("You are wrong !")
elif opr=="-":
    res=num1-num2
    if user==res:
        print("Your are correct !")
    else:
        print("You are wrong !")
elif opr=="*":
    res=num1*num2
    if user==res:
        print("Your are correct !")
    else:
        print("You are wrong !")
elif opr=="/":
    res=num1/num2
    if user==res:
        print("Your are correct !")
    else:
        print("You are wrong !")

