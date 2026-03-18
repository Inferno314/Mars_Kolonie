import pygame
import sys
import random
from Button import Button
from Area import Area
from fieldbutton import FieldButton


class MarsGame:
    def __init__(self):
        pygame.init()

        #game window saved as class attribute
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Mars Game")

        self.clock = pygame.time.Clock()
        
        test_button = Button("B1-D1", 10, 10, 100,100, "blue")
        test_button = set_img("X-Images\FieldEmpty.png")
        test_button2 = Button("B2-D2", 100, 100, 100,100, "red") 
        test_field = FieldButton("F1-D1", 100, 200, 150,400, "yellow")    
        test_rect = Area("R1-D2", 0,80,900,700, (255, 255, 255))
        test_rect2 = Area("R2-D2", 0,0,1200,80, (255, 110, 0)) 
        #First Number: distance from left side, Second: distance from the top, third: lenght from the rect, last: height               
        
        self.drawing_objects = [test_rect, test_rect2, test_button, test_button2, test_field]
        self.clicking_objects = [test_button, test_button2, test_field]
       
    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_window()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for b in self.clicking_objects:
                        b.check_clicked()
            self.window.fill((255, 255, 255))
            for o in self.drawing_objects:
                o.draw(self.window)            

            pygame.display.flip()
            self.clock.tick(60)
            

    def close_window (self):
        sys.exit()