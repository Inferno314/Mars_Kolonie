import pygame

class Area:
    def __init__(self, game, name, x, y, width, height, colour = "white"):
        self.game = game
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
        self.img = None
        self.text = None
        self.textRect = None

    def set_img(self, link):
        self.img = pygame.image.load(link).convert_alpha()
        #self.img.set_colorkey((0,0,0))
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def set_text(self, text, size = 15):
        font = pygame.font.Font('freesansbold.ttf', size)     #textstyle + grösse
        self.text = font.render(text, True, "black")
        self.textRect = self.text.get_rect()
        self.textRect.center = self.rect.center


    def draw(self, window):
        if self.img != None:
            window.blit(self.img, self.rect)
        else:
            pygame.draw.rect(window, self.colour, self.rect)

    
        if self.text != None:
            window.blit(self.text, self.textRect)