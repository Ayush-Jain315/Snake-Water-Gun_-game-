import random
chance=5
print(f"You have {chance} chances ")
lst=["S","W","G"]
while(True):
    computer = 0
    you = 0
    i = 0
    while(i<chance):
        a=random.choice(lst)
        b=input("Enter \"S\" for snake \"W\" for water and \"G\" for gun : ")
        b=b.upper()
        print(f"You choose : {b}")
        print(f"Computer choose : {a}")
        if a==b:
            print("Both have equal choice")
        elif a=="S" and b=="W":
            computer+=1
            print("Snake poisoned the water")
        elif a=="W" and b=="S":
            you+=1
            print("Snake poisoned the water")
        elif a=="S" and b=="G":
            you+=1
            print("gun kills the snake")
        elif a=="G" and b=="S":
            computer+=1
            print("gun kills the snake")
        elif a=="W" and b=="G":
            computer+=1
            print("Gun dipped in water")
        elif a=="G" and b=="W":
            you+=1
            print("Gun dipped in water")
        else:
            print("You choose wrong")
        i+=1
        print(f"Computer scored : {computer}")
        print(f"You scored : {you}")
        print("\n")
    if computer>you:
        print("|You lost|")
    elif computer==you:
        print("Both have equal scores play again to choose who is better ")
    else:
        print("|You win|")

    n=input("if you want to play again press \"Y\" if not press \"N\"")
    n=n.upper()
    if n=="Y":
        continue
    else:
        print("Thank you for playing")
        break