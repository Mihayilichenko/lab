def input_data(train):
    #Ввод данных с клавиатуры
    race = input("Название пункта назначения рейса: ")
    number = input("Номер рейса: ")
    type = float(input("Время: "))
    
    print("Маршрут добавлен!\n")
    input("Нажмите 'Enter' для продолжения")
    #Создание словаря "Маршрут"
    trains = {
        'race': race, 
        'number': number,
        'type': type
    }

    #Добавление маршрута в список
    
    train.append(trains)

    return train

def output_data(train):
    if len(train) == 0:
        print("Ваш список пуст! Сначала добавьте маршруты в список!\n")
        input("Нажмите 'Enter' для продолжения")
    else:
        #Сортировка списка по номеру маршрутов
        train.sort(key=lambda item: item.get('race', ''))

        #Вывод
        for i, route in enumerate(train, 1):
            print(i,".",
                " Начальный пункт: ",route.get('race', ''),";",
                " Номер рейса: ",route.get('number', ''),";",
                " Время отправки: ",route.get('type', 0),";",
                sep=''
                )
        print()
        input("Нажмите 'Enter' для продолжения")
