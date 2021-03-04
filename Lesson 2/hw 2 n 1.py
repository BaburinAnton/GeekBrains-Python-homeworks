int = 1
float = 1.1
str = "Hello world"
list = ['a', '5']
uple = ('b', '6')

list = [int, float, str, list, tuple]
for a in list:
    print(f'{a} is {type(a)}')