int = 1
float = 1.5
str = "Hello world"
list = ['a', '2']
uple = ('b', '3')

super_list = [my_int, my_float, my_str, my_list, my_tuple]
for a in super_list:
    print(f'{a} is {type(a)}')