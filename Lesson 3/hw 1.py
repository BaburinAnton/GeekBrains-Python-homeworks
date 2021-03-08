def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Делитель не может быть равен нулю"
    except ValueError:
        return "Вводимые данные должны быть числом"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))