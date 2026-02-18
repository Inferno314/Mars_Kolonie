import pygame

class Button:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)
    
    
    def get_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("Button got clicked :)")