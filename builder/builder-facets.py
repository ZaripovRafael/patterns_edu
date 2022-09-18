# предоставляет лаконичный интерфейс для 
# поэтапного конструирования сложного объекта


class Person:

    def __init__(self) -> None:
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return (
            f'Address: {self.street_address}, {self.postcode}, '
            f'{self.city} '
            f'\nEmployed at {self.company_name} as a {self.position}, '
            f'earning {self.annual_income}'
        )


class PersonBuilder:
    
    def __init__(self, person=Person()) -> None:  # трюк с = Class() очень важен
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):

    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self
    
    def earning(self, annual_income: str):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person: str) -> None:
        super().__init__(person)
    
    def at(self, street: str):
        self.person.street_address = street
        return self
    
    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self


pb = PersonBuilder()

person = pb\
    .lives\
        .at('221B Backer Street')\
        .in_city('London')\
        .with_postcode('SW12BC')\
    .works\
        .at('Himself')\
        .as_a('Detective')\
        .earning(123000)\
    .build()


print(person)
