from Button import Button

class FieldActionButton(Button):
    def __init__(self, game, myField, name, x, y, width, height, colour = "white"):
        super().__init__(game, name, x, y, width, height, colour)
        self.myField = myField


    def get_clicked(self):
        self.myField.set_type(1)