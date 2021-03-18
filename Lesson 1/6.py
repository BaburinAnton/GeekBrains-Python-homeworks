start_distance = float(input('Введите начальную дистанцию: '))
target_distance = float(input('Введите целевую дистанцию: '))

distance = start_distance
day_counter = 1

while distance < target_distance:
    day_counter += 1
    distance *= 1.1

print('Спортсмен достиг требуемого результата на', day_counter, 'день')
