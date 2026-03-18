import pygame
from Button import Button
from enum import Enum

class FieldTypes(Enum):
    EMPTY = 0
    TEST = 1 
    @classmethod
    def field_colour(cls, type):
        colours = {
            FieldTypes.EMPTY: "green",
            FieldTypes.TEST: "pink"
        }
        return colours[type]


class FieldButton(Button):
    def __init__(self, name, x, y, width, height, colour):
        super().__init__(name, x, y, width, height, colour)
        self.type = FieldTypes.EMPTY
        self.colour = FieldTypes.field_colour(self.type)

    def get_clicked(self):
        self.type = FieldTypes.TEST
        print(self.type)
        self.colour = FieldTypes.field_colour(self.type)        