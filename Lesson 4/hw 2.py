numbers = [55, 42, 1, 67, 14, 9, 11, 8, 13]
list = [el for el in numbers if el > numbers[numbers.index(el)-1]]
print(list)