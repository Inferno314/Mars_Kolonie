import pygame
from Button import Button
from enum import Enum
from FieldActionButton import FieldActionButton

class FieldTypes(Enum):
    EMPTY = 0
    GREEN = 1
    YELLOW = 2
    @classmethod
    def field_colour(cls, type):
        colours = {
            FieldTypes.EMPTY: "green",
            FieldTypes.GREEN: "pink"
        }
        return colours[type]
    
    @classmethod
    def field_img(cls, type):
        Images  = {
            FieldTypes.EMPTY: "X-images/FieldEmpty.png",
            FieldTypes.GREEN: "X-Images/FieldGreen.png"
        }
        return Images[type]


class FieldButton(Button):
    def __init__(self, game, name, x, y, width, height, colour = "white"):
        super().__init__(game, name, x, y, width, height, colour)
        self.type = FieldTypes.EMPTY
        #self.colour = FieldTypes.field_colour(self.type)
        self.set_img(FieldTypes.field_img(self.type))

    def set_type(self, type):
        self.type = FieldTypes(type)
        self.colour = FieldTypes.field_colour(self.type)
        self.set_img(FieldTypes.field_img(self.type)) 
    
    def get_clicked(self):       
        a = self.game.get_area("ActionArea")   
        a.set_text(self.name)
        a.remove_all_children()
        
        if self.type == FieldTypes.EMPTY:
            greenBtn = FieldActionButton(self.game, self, "Gras", 910, 90, 280, 30, "dark green")
            greenBtn.set_text("gras", 20)
            a.add_child(greenBtn)  

            yelBtn = FieldActionButton(self.game, self, "yel", 910, 140, 280, 30, "dark green")
            yelBtn.set_text("yel", 20)
            a.add_child(yelBtn)  

        elif self.type == FieldTypes.GREEN:
            watBtn = FieldActionButton(self.game, self, "Water", 910, 90, 280, 30, "dark green")
            watBtn.set_text("Water", 20)
            a.add_child(watBtn)  

        elif self.type == FieldTypes.YELLOW:
            harvBtn = FieldActionButton(self.game, self, "Harvest", 910, 90, 280, 30, "dark green")
            harvBtn.set_text("Harvest", 20)
            a.add_child(harvBtn)  
