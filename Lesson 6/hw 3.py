class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income


technician = Position('Anton', 'Baburin', 'technician', 28000, 4000)
print(technician.get_full_name(), technician.get_full_profit())