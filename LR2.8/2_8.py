#8. Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
#поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
#с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
#быть упорядочены по номерам поездов; вывод на экран информации о поезде, номер
#которого введен с клавиатуры; если таких поездов нет, выдать на дисплей соответствующее
#сообщение.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
#Список маршрутов
from os import sep

list_route = []

def input_data():
    #Ввод данных с клавиатуры
    start_point = input("Введите начальный пункт маршрута: ")
    number = input("Номер рейса: ")
    time = int(input("Время: "))
    
    print("Маршрут добавлен!\n")
    input("Нажмите 'Enter' для продолжения")
    #Создание словаря "Маршрут"
    route = {
        'start_point': start_point, 
        'number': number,
        'time': time
    }

    #Добавление маршрута в список
    global list_route
    list_route.append(route)

def output_data():
    if len(list_route) == 0:
        print("Ваш список пуст! Сначала добавьте маршруты в список!\n")
        input("Нажмите 'Enter' для продолжения")
    else:
        #Сортировка списка по номеру маршрутов
        list_route.sort(key=lambda item: item.get('number'))

        #Вывод
        for i, route in enumerate(list_route, 1):
            print(i,".",
                " Начальный пункт: ",route.get('start_point', ''),";",
                " Конечный пункт: ",route.get('number', ''),";",
                " Номер маршрута: ",route.get('time', 0),";",
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
    
    