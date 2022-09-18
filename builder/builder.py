class HtmlElement:
    
    indent_size = 2

    def __init__(self, name: str='', text: str=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        
        for element in self.elements:
            lines.append(element.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.__str(0)

class HtmlBuilder:

    def __init__(self, root_name: str):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)
    
    # def add_child(self, child_name: str, child_text: str):
    #     self.__root.elements.append(
    #         HtmlElement(child_name, child_text)
    #     )
    # вместо комментария выше добавим текучий интерфейс вернув self

    def add_child_fluent(self, child_name: str, child_text: str):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self) -> str:
        return str(self.__root)


builder = HtmlBuilder('ul')
builder.add_child_fluent('li', 'Hello')\
    .add_child_fluent('li', 'world')


print('Ordinary builder: ')
print(builder)
