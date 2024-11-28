import pygame

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

class InputBox:
  def __init__(self, size, location):
    self.size = size
    self.location = location

    self.surf = pygame.Surface(size)
    self.surf.fill(white)
    pygame.draw.rect(self.surf, blue, ((0, 0), size), 5)

    self.font1 = pygame.font.Font('../asset/NotoSansKR-Regular.ttf', 48)
    self.font2 = pygame.font.Font('../asset/NotoSansKR-Regular.ttf', 12)

  def update(self, message: str):
    pygame.draw.rect(self.surf, white, ((5, 5), (self.size[0]-10, self.size[1]-10)))
    if message=='Enter a number between 1 and 3':
      text = self.font2.render(message, True, black)
    else:
      text = self.font1.render(message, True, black)
    size = text.get_size()
    self.surf.blit(text, ((self.size[0]-size[0])//2, (self.size[1]-size[1])//2))
    
  def draw(self, screen: pygame.Surface):
    screen.blit(self.surf, (self.location[0]-self.size[0]//2, self.location[1]-self.size[1]//2))

