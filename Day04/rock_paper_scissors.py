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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

options_list = [rock, paper, scissors]

comp_choice = random.choice(options_list)

if user_choice not in [0, 1, 2]:
    print("Invalid choice")
else:
    if user_choice == 0 and comp_choice == scissors:
        print(options_list[0])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You win!")
    elif user_choice == 2 and comp_choice == rock:
        print(options_list[2])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You lose")
    elif user_choice == 1 and comp_choice == scissors:
        print(options_list[1])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You lose")
    elif user_choice == 2 and comp_choice == paper:
        print(options_list[2])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You win!")
    elif user_choice == 0 and comp_choice == paper:
        print(options_list[0])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You lose")
    elif user_choice ==1 and comp_choice == rock:
        print(options_list[1])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("You win!")
    else:
        print(options_list[user_choice])
        print("\nComputer Chose:\n")
        print(comp_choice)
        print("It's a draw")
