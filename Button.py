import pygame
from Area import Area

class Button(Area):
    def __init__(self,game, name, x, y, width, height, colour = "white"):
        super().__init__(game, name, x, y, width, height, colour)
        self.counter = 0

    
    
    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.get_clicked()


    def get_clicked(self):
        print(f"Button clicked: {self.name}")
        self.game.react(self.name, "ActionArea", "open")  