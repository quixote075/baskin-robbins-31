import sys, pygame, player
from player.strategy import HumanStrategy4Player, ComputerStrategy
from entity import InputBox, IceCreams

white = (255, 255, 255)
black = (0, 0, 0)

class GameModel:
  def __init__(self):
    self.human_strategy = HumanStrategy4Player()
    self.computer_strategy = ComputerStrategy()
    self.play = player.GameContext(self.human_strategy, self.computer_strategy)

  def update(self):
    self.play.next_turn()

class GameView:
  def __init__(self):
    pygame.init()

    self.screen = pygame.display.set_mode([640, 480])
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font('../asset/NotoSansKR-Regular.ttf', 40)

    self.input_box = InputBox([200, 100], [320, 150])
    self.ice_creams = IceCreams([48, 48], [86, 270])
    self.past_count = 0 # Backtrace the choosed number

  def update(self, number):
    self.input_box.update(number)
    self.draw_game_state(self.game_state)

  def draw_game_state(self, game_state):
    self.screen.fill(white)

    text = self.font.render(f'{game_state.play.state.id} turn', True, black)
    size = text.get_size()
    self.screen.blit(text, (320-size[0]//2, 50-size[1]//2))

    self.ice_creams.update(game_state.play.count-self.past_count)
    self.ice_creams.draw(self.screen)
    
    self.input_box.draw(self.screen)

    self.game_state = game_state
    self.past_count = game_state.play.count

    self.input_box.update('')

    pygame.display.update()
    self.clock.tick(60)

  def draw_winner(self, winner):
    self.screen.fill(white)

    text = self.font.render(f'Game over, {winner} lose!', True, black)
    size = text.get_size()
    self.screen.blit(text, (320-size[0]//2, 240-size[1]//2))

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    self.clock.tick(60)

class GameController:
  def __init__(self, model, view):
    self.model = model
    self.view = view

    self.model.human_strategy.attach(self.view)

  def game_play(self):
    while True:
      if self.model.play.count<31:
        if self.model.play.state.id=='you':
          self.view.input_box.update('Enter a number between 1 and 3')
        self.view.draw_game_state(self.model)
        self.model.update()
      else:
        self.view.draw_winner(self.model.play.state.id)

def vs_computer():
  model = GameModel()
  view = GameView()
  controller = GameController(model, view)

  controller.game_play()

if __name__=='__main__':
  vs_computer()