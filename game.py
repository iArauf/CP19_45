import pygame

class BoxesGame():
    def __init__(self):
        pass
    
        pygame.init()
        width, height = 389, 489
     
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")
        
        self.clock=pygame.time.Clock()
    def update(self):
        self.clock.tick(60)

        self.screen.fill(0)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()

bg=BoxesGame()
while 1:
    bg.update()