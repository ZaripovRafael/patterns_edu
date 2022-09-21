"""
Мотивация использования:
    Логика создания объекта становится слишком запутанной
    Конструктор недостаточно выразителен
        - Назван всегда __init__
        - Невозможно перегрузить одним и тем же набором аргументов 
            с разными именами
        - Может превратиться в "ад опциональных параметров"
    
    Полное создания объекта (не пошагово, как делал Строитель)
        можно отдать на "аутсорсинг"

        - Отдельному методу (фабричный метод)
        - Отдельному классу (Фабрика)
        - Можно создать иерархию Фабрик с помощью Абстрактной фабрики

Фабрика - компонент, отвечающий исключительно за полное (не пошаговое)
          создание объектов.
"""


from enum import Enum
from math import cos, sin

class CoordinateSystem(Enum):
    """
    
    """
    CARTESIAN = 0
    POLAR = 1


class Point:
    """
    Предположим что нам нужно создавать точку в пространстве.
    И по началу нам достаточно двук координат в декардовой системе

    Но позже нам захотелось добавить поддержку полярных координат,
    а второй __init___ в Рoint уже не прописать
    По этому мы определяем класс CoordinateSystem, в котором будем хранить
    типы системы счислений.
    После этого мы должны дать имена переменным, которые не подразумевают
    конкретной системы счисления (заменили x, y на a, b
    Этот подход не рациональный - так как если нам нужно будет добавить
    еще какую-то систему, то придется писать под  нее отдльную реализацию,
    нарушая принцип открытости закрытости.
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return (f'point_1 = {self.x} '
                f'point_2 = {self.y}')

    # def __init__(self, a, b, system: CoordinateSystem= CoordinateSystem.CARTESIAN) -> None:
        
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.polar:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    class PointFactory:
        """
        Все что мы по сути сделали - вынели в подкласс
        фабрикметоды, можно и вовсе в отдельный класс вынести,
        но тогда пользователю будет непонятно есть ли
        фабрика или нет.
        """
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)
        
        @staticmethod
        def new_polar_point(rho, theta):
            return Point(
                rho * cos(theta),
                rho * sin(theta)
            )


if __name__ == '__main__':

    p = Point(3, 4)

    print('Standart creat: ')
    print(p)

    print('\nWith fabric: ')
    p_cart = Point.PointFactory.new_cartesian_point(3, 4)
    print(p_cart)

    print('\nWith fabrick (polar): ')
    p_pol = Point.PointFactory.new_polar_point(3, 4)
    print(p_pol)
