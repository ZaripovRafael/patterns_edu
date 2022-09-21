"""
Мотивация:
    - Сложные объекты не создаются с нуля
      они повторяют существующие конструкции
    - Существующий проект (класс) является Прототипом
    - Мы делаем копию объекта-прототипа
      и изменяем его
    - мы делаем клонирование удобным (например, через Фабрики)

Прототип - частично или полностью инициализированный объект,
           который клонируется и используется.
"""
import copy


class Address:

    def __init__(self, street_address, city, country) -> None:
        self.street_address = street_address
        self.city = city
        self.country = country
    
    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:

    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'name = {self.name}\naddress = {self.address}'


print('Будет работать неправильно\n')
john = Person('Джон', Address('221B Backer Street', 'London', 'UK'))
jane = john
jane.name = 'Джейн'

print('John\n', john, '\n')
print('Jane\n',jane, '\n')

print('Будет работать правильно\n')
john = Person('Джон', Address('221B Backer Street', 'London', 'UK'))
jane = copy.deepcopy(john)
jane.name = 'Джейн'
jane.address.city = 'Birmingham'

print('John\n', john, '\n')
print('Jane\n',jane, '\n')
