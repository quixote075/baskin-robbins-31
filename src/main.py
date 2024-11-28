import player
from player.strategy import HumanStrategy, ComputerStrategy

class GameModel:
  def __init__(self):
    human_strategy = HumanStrategy()
    computer_strategy = ComputerStrategy()
    self.play = player.GameContext(human_strategy, computer_strategy)
  
  def update(self):
    self.play.next_turn()

class GameView:
  def display_game_state(self, game_state):
    print('\tcurrent number is..', game_state.count)

  def display_winner(self, winner):
    print(f'Game over, {winner} lose!\n')

class GameController:
  def __init__(self, model, view):
    self.model = model
    self.view = view

  def game_play(self):
    while self.model.play.count<31:
      self.model.update()
      self.view.display_game_state(self.model.play)
    self.view.display_winner(self.model.play.state.id)
    input('Press ENTER to exit the program')

def vs_computer():
  model = GameModel()
  view = GameView()
  controller = GameController(model, view)

  controller.game_play()

if __name__=='__main__':
  vs_computer()
