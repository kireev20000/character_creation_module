from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def calculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. \
          Это будет: {calculateSquareRoot(your_number)}')

print(message)
calc (25.5)


 находчивый воин дальнего боя. Обладает высоким интеллектом
^