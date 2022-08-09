# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    CRAWL_SPEED_COEFFICIENT = 0.5
    FLY_SPEED_COEFFICIENT = 1.5

    def __init__(self, field, x: int, y: int, movement_type: str):
        """
        :param field: игровое поле
        :param x: координата
        :param Y: координата
        :param movement_type: может 'ползти' и 'лететь'
        """
        self._field = field
        self._x = x
        self._y = y
        self._movement_type = movement_type

    def _calculate_speed(self, speed):
        if self._movement_type == "fly":
            return speed * self.FLY_SPEED_COEFFICIENT
        elif self._movement_type == "crawl":
            return speed * self.CRAWL_SPEED_COEFFICIENT

    def move(self, destination, speed):
        speed = self._calculate_speed(speed)

        if destination == 'UP':
            self._field.set_unit(y=self._y + speed, x=self._x, unit=self)
        elif destination == 'DOWN':
            self._field.set_unit(y=self._y - speed, x=self._x, unit=self)
        elif destination == 'LEFT':
            self._field.set_unit(y=self._y, x=self._x - speed, unit=self)
        elif destination == 'RIGTH':
            self._field.set_unit(y=self._y, x=self._x + speed, unit=self)
