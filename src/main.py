import player
from player.strategy import HumanStrategy, ComputerStrategy

class Game:
  def __init__(self):
    human_strategy = HumanStrategy()
    computer_strategy = ComputerStrategy()
    self.play = player.GameContext(human_strategy, computer_strategy)

  def run(self):
    while self.play.count<31:
      self.play.next_turn()
      print('\tcurrent number is..', self.play.count)
    print(f'Game over, {self.play.state.id} lose!')

def main():
  game = Game()
  game.run()

if __name__=='__main__':
  main()