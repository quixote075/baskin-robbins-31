from .state import HumanState, ComputerState

class GameContext:
  def __init__(self, human_strategy, computer_strategy):
    self.state = HumanState()
    self.human_strategy = human_strategy
    self.computer_strategy = computer_strategy
    self.count = 0
  
  def set_state(self, state):
    self.state = state
  
  def next_turn(self):
    self.state.next_turn(self)

