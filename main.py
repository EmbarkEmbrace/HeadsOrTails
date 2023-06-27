import random

Toss = random.choice(["Heads", "Tails"])
Call = input("Hi, Let's flip a coin. Are you calling Heads, or Tails?\n").capitalize()
if Call == Toss:
  print(f'The coin landed on {Toss}, you win!')
else:
  print(f'The coin landed on {Toss}, you lose!')