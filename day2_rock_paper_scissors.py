import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
comp_choice = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <=2:
    print(f"You Chose: \n{choices[user_choice]}")
else:
    print("Invalid input. You lose.")

if user_choice > 0 and user_choice <= 2:
    print("Computer Chose: ")

    print(choices[comp_choice])

    if comp_choice == user_choice:
        print("It's a draw")
    elif comp_choice == 0 and user_choice == 1:
        print("You win")
    elif comp_choice == 1 and user_choice == 0:
        print("You lose")
    elif comp_choice == 1 and user_choice == 2 :
        print("You win")
    elif comp_choice == 2 and user_choice == 1:
        print("You lose")
    elif comp_choice == 2 and user_choice == 0:
        print("You Win")
    elif comp_choice == 0 and user_choice == 2:
        print("You lose")
    else:
        print("Invalid input. You lose.")