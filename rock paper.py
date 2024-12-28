"""
1. Input from user(Rock,paper,scissor)
2. Computer choice(computer will choose randomly not conditionally)
3. Result print

"""
import random

item_list=["Rock", "Paper", "Scissor"] 

user_choice= input("Enter Your move=Rock,Paper,Scissor=")
comp_choice=random.choice(item_list)

print(f"User choice={user_choice},computer choice={comp_choice}")

if user_choice=="comp_choice":
    print("both chooses same: = Match Tie")  

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers Rock= Win computer")
    else:
        print("Rock smases scissor= You win")

elif user_choice=="Paper":
    if comp_choice=="scissor":
        print("scissor cuts paper, Win computer")
    else:
        print("Paper cover rock")

elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissor cuts paper, You win")
    else:
        print("Rock smases Scissor, Computer win")


    
  