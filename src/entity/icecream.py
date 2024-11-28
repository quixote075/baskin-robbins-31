import os, pygame

white = (255, 255, 255)
apple_mint = (127, 255, 212)
black = (0, 0, 0)

class IceCream:
  counter = 0
  def __init__(self, size, location):
    IceCream.counter += 1

    self.size = size
    self.location = location

    self.surf = pygame.Surface(size)
    self.surf.fill(white)
    pygame.draw.circle(self.surf, apple_mint, (size[0]//2, size[1]//2), size[0]//2)

    self.font = pygame.font.Font(os.path.join('asset', 'NotoSansKR-Regular.ttf'), 24)
    text = self.font.render(str(IceCream.counter), True, black)
    size = text.get_size()
    self.surf.blit(text, ((self.size[0]-size[0])//2, (self.size[1]-size[1])//2))
  
  def draw(self, screen):
    screen.blit(self.surf, (self.location[0]-self.size[0]//2, self.location[1]-self.size[1]//2))

class IceCreams:
  def __init__(self, size, location, margin = 52):
    self.ice_creams = []
    for i in range(10):
      self.ice_creams.append(IceCream(size, (location[0]+margin*i, location[1])))
    for j in range(11):
      self.ice_creams.append(IceCream(size, (location[0]+margin*j-margin//2, location[1]+margin)))
    for k in range(10):
      self.ice_creams.append(IceCream(size, (location[0]+margin*k, location[1]+margin*2)))
    
  def update(self, number):
    self.ice_creams = self.ice_creams[number:]

  def draw(self, screen):
    for ice_cream in self.ice_creams:
      ice_cream.draw(screen)
