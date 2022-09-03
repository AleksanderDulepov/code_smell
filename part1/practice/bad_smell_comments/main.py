class Unit:
    # ...
    def movement_init_on_field(self, field, x_coord, y_coord, direction, is_fly, is_crawl, speed_base=1):
        """Функция реализует перемещение юнита по полю."""

        # проверка валидности ввода метода перемещения юнита
        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        # координаты перемещений для полета
        if is_fly:
            speed_base *= 1.2
        if direction == 'UP':
            new_y = y_coord + speed_base
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed_base
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord
        elif direction == 'RIGHT':
            new_y = y_coord
            new_x = x_coord + speed_base

        # координаты перемещений для ползания
        if is_crawl:
            speed_base *= 0.5
        if direction == 'UP':
            new_y = y_coord + speed_base
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed_base
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord
        elif direction == 'RIGHT':
            new_y = y_coord
            new_x = x_coord + speed_base

            # выполнение перемещения юнита
            field.set_unit(x=new_x, y=new_y, unit=self)
