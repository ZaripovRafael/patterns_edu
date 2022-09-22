"""
Если у нас всего несколько предопределенных
прототипов во всем приложении, то было бы 
не плохо сделать для них фабрику, которая
позволит делать копии протатипов, без неоюходимости
копировать их вручную
"""
import copy


class Address:

    def __init__(
        self,
        street_address: str,
        suite: int,
        city: str
        ) -> None:
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self) -> str:
        return (
            f'{self.street_address}, Suite #{self.suite}, '
            f'{self.city}'
            )


class Employee:

    def __init__(
        self,
        name: str,
        address: Address
        ) -> None:
        self.address = address
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:

    main_office_employee = Employee(
        '',
        Address('Oktabrya pr 4/3', 0, 'Ufa')
        )
    
    aux_office_employee = Employee(
        '',
        Address('Oktabrya pr 4/2E', 0, 'Ufa')
        )

    @staticmethod
    def __new_employee(proto , name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )
    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )


rafael = EmployeeFactory.new_main_office_employee('Rafael', 111)
adelina = EmployeeFactory.new_aux_office_employee('Adelina', 10)

print(rafael)
print()
print(adelina)