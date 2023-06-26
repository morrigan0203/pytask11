
from time import time

class MyString(str):
    """ Расширяем клас str полем имя и время создания. """

    def __new__(cls, value: str, name: str):
        """ Расширяем метод создания параметрами имя и время создания """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time()
        return instance
    
    def __str__(self) -> str:
        return f'Строка с именем {self.name} и время создание {self.created_at}'
    
    def __repr__(self) -> str:
        return f'MyString("{super().__str__()}", "{self.name}")'

if __name__=="__main__":
    s = MyString("MyString UPPER CASE, lowwer case", "KS")
    print(s.name, s.created_at)
    print(s)
    print(s.upper())
    print(s.lower())
    print(f'{s = }')

    #help(MyString)
