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
game_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[player])

    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if player == 0 and computer_choice == 2:
        print("You win!")
    elif player == 0 and computer_choice == 0:
        print("It's a Draw")
    elif player == 0 and computer_choice == 1:
        print("You lose :(")
    elif player == 1 and computer_choice == 0:
        print("You Win!")
    elif player == 1 and computer_choice == 1:
        print("It's a Draw")
    elif player == 1 and computer_choice == 2:
        print("You lose :(")
    elif player == 2 and computer_choice == 0:
        print("You lose :(")
    elif player == 2 and computer_choice == 1:
        print("You win!")
    elif player == 2 and computer_choice == 2:
        print("It's a Draw")
