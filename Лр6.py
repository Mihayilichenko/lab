#Ключи: название начального пункта маршрута; название конечного пункта маршрута; 
#номер маршрута. Ввод с клавиатуры данных в список, записи упорядочены по 
#номерам маршрутов. Вывод маршрута номер которого ввели с клав. , если нет - сообщить

import os
#Список маршрутов
from os import sep

train = []

def input_data():
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
    global train
    train.append(trains)

def output_data():
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
                " Тип поезда: ",route.get('type', 0),";",
                sep=''
                )
        print()
        input("Нажмите 'Enter' для продолжения")

while True:
    os.system('cls')
    print("Заполнить список >> [1]")
    print("Вывод списка >> [2]")
    print("Выход >> [3]")
    
    command = int(input(">>"))
    
    if command == 1:
        input_data()
               
    elif command == 2:
        output_data()

    elif command == 3:
        break
    else:
        print(f"Неизветсная команда: {command}\n")
        input("Нажмите 'Enter' для продолжения")
    
    