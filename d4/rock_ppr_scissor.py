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

image_list = [rock, paper, scissors]

your_response = int(input("Please enter your response here, 0 for rock, 1 for paper 2 for scissors.\n"))
print(image_list[your_response])

computer_response = (random.randint(0, 2))
print("Computer response:")
print(image_list[computer_response])
if your_response == 2 and computer_response == 0:
    print("You lose")
elif your_response == 0 and computer_response == 2:
    print("You won")
elif computer_response > your_response:
    print("Computer Wins")
elif computer_response < your_response:
    print("You Win")
elif computer_response == your_response:
    print("It's a draw")
elif your_response >= 3 or your_response < 0:
    print("You typed an invalid number, you lose!")





