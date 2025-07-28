# 4.4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        self.start = False

    def start(self):
        if not self.start:
            self.start = True
            print('Автомобиль заведен')

    def stop(self):
        if self.start:
            self.start = False
            print('Автомобиль заглушен')

    def set_year(self, new_year: int):
        self.year = new_year

    def set_type(self, new_type):
        self.type = new_type

    def set_color(self, new_color):
        self.color = new_color