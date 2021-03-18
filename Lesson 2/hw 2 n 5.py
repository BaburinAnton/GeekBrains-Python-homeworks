raiting = []

while True:
    item = input('Введите число: ')
    if not item.isdigit():
        print("Введены некорректные данные.")
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(raiting):
        if item > num:
            idx = i
            break

    if idx is None:
        raiting.append(item)
    else:
        raiting.insert(idx, item)

    print(raiting)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break
