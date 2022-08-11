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

# Write your code below this line 👇
pics = [rock, paper, scissors]

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(pics[playerChoice])

compChoice = random.randint(0, 2)

print(pics[compChoice])

choiceMatrix = [["It's a Draw!", "You Lose!", "You Win!"],
                ["You Win!", "It's a Draw!", "You Lose!"],
                ["You Lose!", "You Win!", "It's a Draw!"]]

print(choiceMatrix[playerChoice][compChoice])
