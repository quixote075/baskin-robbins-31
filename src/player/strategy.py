import random

class ComputerStrategy:
  def __init__(self):
    self.index = 0
    self.numbers = [2, 6, 10, 14, 18, 22, 26, 30, 31]
  def choose_number(self, current_count):
    if current_count>=self.numbers[self.index]:
      self.index += 1
    diff = self.numbers[self.index]-current_count
    if diff<=3:
      return diff
    return random.randint(1, 3)

class HumanStrategy:
  def choose_number(self, current_count):
    while True:
      try:
        number = int(input('- Enter a number between 1 and 3: '))
        if current_count+number>31:
          return 31-current_count
        if 1<=number<=3:
          return number
        print('[ERR] Please enter a number between 1 and 3.')
      except ValueError:
        print('[ERR] Invalid input. Please enter an integer.')
