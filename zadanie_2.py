

class Archive:
    """ Клас Archive содержит параметры всех инстансов класса Archive """

    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """ Заполняем переменные списки входными параметрами number и value """
        instance = super().__new__(cls)
        instance.numbers.append(number)
        instance.values.append(value)
        return instance
    
    def __init__(self, number: int, value: str):
        """ Инициируем параметры number и value нового инстанса Archive """
        self.number = number
        self.value = value
    
    def __str__(self) -> str:
        return f'Архив со значениями {self.number} и {self.value}'
    
    def __repr__(self) -> str:
        return f'Archive({self.number},"{self.value}")'

if __name__=="__main__":
    a = Archive(10, "val")
    a2 = Archive(20, "val2")
    print(a,a2)
    print(f'{a.numbers}', f'{a.values}')
    print(f'{a2.numbers}', f'{a2.values}')
    a3 = Archive(30, "val3")
    print(f'{a3.numbers}', f'{a3.values}')
    #help(Archive)
    print(f'{a}')
    print(f'{a2 = }')
