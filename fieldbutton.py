import pygame
from Button import Button
from enum import Enum

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
    def __init__(self, name, x, y, width, height, colour = "white"):
        super().__init__(name, x, y, width, height, colour)
        self.type = FieldTypes.EMPTY
        #self.colour = FieldTypes.field_colour(self.type)
        self.set_img(FieldTypes.field_img(self.type))

    def get_clicked(self):
        self.type = FieldTypes.GREEN
        print(self.type)
        #self.colour = FieldTypes.field_colour(self.type)
        self.set_img(FieldTypes.field_img(self.type))               