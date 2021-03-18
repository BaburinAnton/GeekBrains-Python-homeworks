from functools import reduce

def func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(func, [el for el in range(99, 1001) if el % 2 == 0])}')