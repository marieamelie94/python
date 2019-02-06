import random

class GuessingGame():
  def __init__(self):
    self.rand_choice = random.randint(0,10)

  def reset_random(self):
    print("Reset of the number ...")
    self.rand_choice = random.randint(0,10)

  def guess(self):
    user_guess = int(input("Your guess (0-10?"))
    if user_guess == self.rand_choice:
      print("Correct Guess")
    elif user_guess < self.rand_choice:
      print("Wrong guess, go higher, call the guess function again")
    else:
      print("Wrong guess, go lower, call the guess function again")

g = GuessingGame()

g.rand_choice

g.guess()
