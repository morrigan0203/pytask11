

class Matrix:
    """ Клас представляем двумерную матрицу """

    def __init__(self, data: list):
        """  """
        self.data = data

    def __str__(self) -> str:
        return f"Матрица размером {len(self.data[0])} на {len(self.data)}"

    def __repr__(self) -> str:
        j1,j2 = ","," "
        res = j2.join([j2.join([str(e) for e in sub]) for sub in self.data])
        return res

    def __add__(self, other):
        res = []
        for i in range(len(self.data)):
            res.append([])
            for j in range(len(self.data[0])):
                r = self.data[i][j] + other.data[i][j]
                res[i].append(r)
        return res

    def __mul__(self, other):
        res = []
        for i in range(len(self.data)):
            res.append([])
            for j in range(len(self.data[0])):
                e = 0
                for k in range(len(self.data[0])):
                    e = e + self.data[i][k] * other.data[k][j]
                res[i].append(e)
        return res

    def __eq__(self, other) -> bool:
        """ Переопределяем операцию сравнеия eq, сравниваем """
        return self.data == other.data

    def __ne__(self, other) -> bool:
        """ Переопределяем операцию сравнеия ne, сравниваем """
        return self.data != other.data

    def __gt__(self, other) -> bool:
        """ Переопределяем операцию сравнеия gt, сравниваем """
        return self.data > other.data

    def __ge__(self, other) -> bool:
        """ Переопределяем операцию сравнеия ge, сравниваем """
        return self.data >= other.data

    def __lt__(self, other) -> bool:
        """ Переопределяем операцию сравнеия lt, сравниваем """
        return self.data < other.data

    def __le__(self, other) -> bool:
        """ Переопределяем операцию сравнеия le, сравниваем """
        return self.data <= other.data


if __name__=="__main__":
    d1 = [[1,2,3],[4,5,6],[7,8,9]]
    m1 = Matrix(d1)
    print(f'{m1 = }')

    d2 = [[9,8,7],[6,5,4],[3,2,1]]
    m2 = Matrix(d2)

    m3 = m1 + m2
    print(f'{m3 = }')

    m4 = m1 * m2
    print(f'{m4 = }')

    print(f'm1 == m2 = {m1 == m2}')
    print(f'm1 != m2 = {m1 != m2}')
    print(f'm1 > m2 = {m1 > m2}')
    print(f'm1 >= m2 = {m1 >= m2}')
    print(f'm1 < m2 = {m1 < m2}')
    print(f'm1 <= m2 = {m1 <= m2}')

