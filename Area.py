import pygame

class Area:
    def __init__(self, name, x, y, width, height, colour):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
        self.img = None

    def set_img(self, link):
        self.img = pygame.image.load(link).convert_alpha()

    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)
        if self.img != None:
            window.blit(self.img, self.rect)