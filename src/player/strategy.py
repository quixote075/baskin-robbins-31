import sys, pygame, random, time

class ComputerStrategy:
  def __init__(self):
    self.index = 0
    self.numbers = [2, 6, 10, 14, 18, 22, 26, 30, 31]
  def choose_number(self, current_count):
    time.sleep(1)
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

class HumanStrategy4Player:
  def __init__(self):
    self.observers = []

  def choose_number(self, current_count):
    while True:
      number = int(self.my_input())
      if current_count+number>31:
        return 31-current_count
      if 1<=number<=3:
        return number
      print('[ERR] Please enter a number between 1 and 3.')
      
  def my_input(self) -> int:
    self.number = 0
    while True:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_RETURN:
            return int(self.number)
          elif event.unicode.isdigit():
            self.number = event.unicode
            self.notify(self.number)

  def attach(self, observer):
    self.observers.append(observer)
  
  def detach(self, observer):
    self.observers.remove(observer)
  
  def notify(self, message):
    for observer in self.observers:
      observer.update(message)
      