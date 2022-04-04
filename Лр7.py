#Ключи: название начального пункта маршрута; название конечного пункта маршрута; 
#номер маршрута. Ввод с клавиатуры данных в список, записи упорядочены по 
#номерам маршрутов. Вывод маршрута номер которого ввели с клав. , если нет - сообщить

import os
import Data
#Список маршрутов
from os import sep

train = []

while True:
    os.system('cls')
    print("Заполнить список >> [1]")
    print("Вывод списка >> [2]")
    print("Выход >> [3]")
    
    command = int(input(">>"))
    
    if command == 1:
        train = Data.input_data(train)
               
    elif command == 2:
       Data.output_data(train)

    elif command == 3:
        break
    else:
        print(f"Неизветсная команда: {command}\n")
        input("Нажмите 'Enter' для продолжения")
    
    