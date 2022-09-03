class Unit:
    field = Field()

    def __init__(self, x_coord, y_coord, method_move, speed):
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._method_move = method_move
        self._speed = self._get_speed(self, speed)


    def move(self, direction):
        if direction == 'UP':
            new_y = self._y_coord + self._speed
            new_x = self._x_coord
            self._get_move(new_x, new_y)
        elif direction == 'DOWN':
            new_y = self._y_coord - self._speed
            new_x = self._x_coord
            self._get_move(new_x, new_y)
        elif direction == 'LEFT':
            new_y = self._y_coord
            new_x = self._x_coord - self._speed
            self._get_move(new_x, new_y)
        elif direction == 'RIGTH':
            new_y = self._y_coord
            new_x = self._x_coord + self._speed
            self._get_move(new_x, new_y)


    def _get_speed(self, speed):
        if self._method_move == "fly":
            return speed * 1.2
        elif self._method_move == "crawl":
            return speed * 0.5
        raise ValueError('Рожденный ползать летать не должен!')


    def _get_move(self, new_x, new_y):
        field.set_unit(x=new_x, y=new_y, unit=self)
