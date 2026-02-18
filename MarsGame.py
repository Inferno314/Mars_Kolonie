import pygame
import sys
import random
from Button import Button

class MarsGame:
    def __init__(self):
        pygame.init()

        #game window saved as class attribute
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Mars Game")

        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_window()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_clicked()
            
            self.window.fill(255, 255, 255)
            
            test_rect = pygame.Rect(0,0,1200,80)
            #First Number: distance from left side, Second: distance from the top, third: lenght from the rect, last: height
            pygame.draw.rect(self.window, (255, 255, 255), test_rect)

            test_rect = pygame.Rect(0,80,900,700)
            pygame.draw.rect(self.window, (255, 110, 0), test_rect)
            
            test_button = Button(10, 10, 100,100, "blue")
            test_button.draw(self.window)
            
            test_button2 = Button(1000, 1000, 100,100, "red")
            test_button2.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)
            

    def close_window (self):
        sys.exit()