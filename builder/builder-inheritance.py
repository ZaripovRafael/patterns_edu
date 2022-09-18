"""
Строитель через наследования решает проблему с 
нарушением принципа "открытости закрытости",
так как корневой строитель никак не зависит от
последующих. Они наследуются друг от друга по цепочке,
добавляя функциональности. 
"""


class Person:

    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self) -> str:
        return (
            f'{self.name} born on {self.date_of_birth} '
            f'work as {self.position}'
        )

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()
    
    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):

    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):

    def work_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):

    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()

me = pb\
    .called('Rafael')\
    .work_as_a('Engeneer')\
    .born('28-04-1993')\
    .build()

print(me)