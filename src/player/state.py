class ComputerState:
  id = 'computer'
  def next_turn(self, context):
    number = context.computer_strategy.choose_number(context.count)
    context.count += number
    print(f'Computer pick {number}')
    if context.count==31:
      return
    context.set_state(HumanState())

class HumanState:
  id = 'you'
  def next_turn(self, context):
    number = context.human_strategy.choose_number(context.count)
    context.count += number
    print(f'Human pick {number}')
    if context.count==31:
      return
    context.set_state(ComputerState())
