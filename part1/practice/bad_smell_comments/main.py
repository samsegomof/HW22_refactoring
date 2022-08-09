# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def __init__(self, field, x: int, y: int, state: str, speed: int, movement_type: str):
        """
        :param field: игровое поле
        :param x: x-координата
        :param y: у-координата
        :param state: может "ползти" или "лететь"
        """
        self._field = field
        self._x = x
        self._y = y
        self._movement_type = movement_type
        self._speed = speed

    def move(self, destination):
        """Передвижение объекта"""
        speed = self._calc_speed(self._speed)
        up_state = self._field.set_unit(y=self._y + speed, x=self._x, unit=self)
        down_state = self._field.set_unit(y=self._y - speed, x=self._x, unit=self)
        right_state = self._field.set_unit(y=self._y, x=self._x + speed, unit=self)
        left_state = self._field.set_unit(y=self._y, x=self._x - speed, unit=self)

        states = {'UP': up_state,
                  'DOWN': down_state,
                  'RIGHT': right_state,
                  'LEFT': left_state
                  }
        if destination == states['UP']:
            return up_state
        elif destination == states['DOWN']:
            return down_state
        elif destination == states['RIGHT']:
            return right_state
        elif destination == states['LEFT']:
            return left_state

    def _calc_speed(self, fly_coefficient=1.5, crawl_coefficient=0.5):
        """Расчет скорости основанный на состоянии объекта"""
        if self._movement_type == 'FLY':
            return self._speed * fly_coefficient
        elif self._movement_type == 'СRAWL':
            return self._speed * crawl_coefficient

