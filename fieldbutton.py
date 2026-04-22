import pygame
from Button import Button
from enum import Enum
from FieldActionButton import FieldActionButton

class FieldTypes(Enum):
    EMPTY = 0
    GREEN = 1 
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
        self.game.react(self.name, "ActionArea", "open")  
        self.type = FieldTypes.GREEN
        print(self.type)
        #self.colour = FieldTypes.field_colour(self.type)
        #self.set_img(FieldTypes.field_img(self.type))       
        a = self.game.get_area("ActionArea")   
        a.set_text(self.name)  
        unlockBtn = FieldActionButton(self.game, self, "Unlock", 910, 90, 280, 30, "dark green")
        unlockBtn.set_text("unlock Field", 20)
        a.add_child(unlockBtn)  
        #self.game.add_button_to_game(unlockBtn) 
