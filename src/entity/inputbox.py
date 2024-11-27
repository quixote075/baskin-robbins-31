import pygame

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

class InputBox:
  def __init__(self, size, location):
    self.surf = pygame.Surface(size)
    self.surf.fill(white)
    pygame.draw.rect(self.surf, blue, ((0, 0), size), 5)
    self.font = pygame.font.Font('../asset/NotoSansKR-Regular.ttf', 48)
    self.observers = []
    self.text = '0'
    self.size = size
    self.location = location
  
  def input_handler(self, event: pygame.event):
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_1:
        self.update('1')
      if event.key==pygame.K_2:
        self.update('2')
      if event.key==pygame.K_3:
        self.update('3')
      if event.key==pygame.K_RETURN:
        self.update('0')

  def update(self, input_number: str):
    pygame.draw.rect(self.surf, white, ((5, 5), (self.size[0]-10, self.size[1]-10)))
    if input_number!='0':
      text = self.font.render(input_number, True, black)
      size = text.get_size()
      self.surf.blit(text, ((self.size[0]-size[0])//2, (self.size[1]-size[1])//2))
    elif self.text!='0':
      self.notify()
    self.text = input_number

  def draw(self, screen: pygame.Surface):
    screen.blit(self.surf, (self.location[0]-self.size[0]//2, self.location[1]-self.size[1]//2))

  def attach(self, observer):
    self.observers.append(observer)
  
  def detach(self, observer):
    self.observers.remove(observer)
  
  def notify(self):
    for observer in self.observers:
      observer.update(self.text)
