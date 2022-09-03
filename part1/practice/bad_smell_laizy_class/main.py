class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field):
        field.set_unit(self.x, self.y, self)


class Field:
    def set_unit(self, x, y, unit: Unit):
        pass


class Main:
    def __init__(self):
        self.field = Field()
        self.unit = Unit()
        self.unit.move(field=self.field)
