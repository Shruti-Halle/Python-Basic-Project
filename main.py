import random
'''
Snake=1
Water=-1
Gun=0
'''
computer=random.choice([1,0,-1])
yourstr=input("Enter your choice:")
yourDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you = yourDict[yourstr]

#By now we have two choices(variables),you and computer

print(f"Your choice is:{reverseDict[you]}\n Computer's choice is:{reverseDict[computer]}")

if(computer == you):
    print("It's a draw!")
#1=SNAKE -1=WATER 0=GUN
else:
    if(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    else:
        print("Something went wrong")
    