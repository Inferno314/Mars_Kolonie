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
        
        resArea = Area(self, "ResourceDisplay", 0, 0, 1200, 80, "light blue")
        resArea.set_text("Resources", 50)
        
        colArea = Area(self,"ColonyArea", 0, 80, 900, 720)
        colArea.set_img("X-Images/floor_desert.png")
        field1= FieldButton(self, "F1", 20, 100, 50 , 50)

        actArea = Area(self,"ActionArea", 900, 80, 300, 720, "gray")
        actArea.set_text("Actions", 30)
        unlockBtn = Button(self, "Unlock", 910, 90, 280, 30, "dark green")
        unlockBtn.set_text("unlock Field", 20)

        #First Number: distance from left side, Second: distance from the top, third: lenght from the rect, last: height               
        
        self.drawing_objects = [resArea, colArea ,actArea, field1, unlockBtn]
        self.clicking_objects = [field1, unlockBtn]
       
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
            
def react(self, source_name, target_name, action_type):
    for o in self.drawing_objects:
        if o.name == target_name:
            o.set_text(source_name)


    def close_window (self):
        sys.exit()