numbers = [14, 42, 1, 7, 13, 99, 16, 1, 70, 55, 14, 13, 1, 7]
list = [el for el in numbers if numbers.count(el)==1]
print(list)