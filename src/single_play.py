import sys
import pygame
from entity.inputbox import InputBox

def vs_computer():
  pygame.init()

  screen = pygame.display.set_mode((640, 480))
  clock = pygame.time.Clock()

  white = (255, 255, 255)

  input_box = InputBox([160, 100], [320, 120])

  while True:
    screen.fill(white)
    input_box.draw(screen)

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      input_box.input_handler(event)

    pygame.display.update()
    clock.tick(60)

if __name__=='__main__':
  vs_computer()