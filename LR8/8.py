#8. Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
#должен включать в себя не менее четырех функций инициализации: числами, строкой
#(например, «23:59:59»), секундами и временем. Обязательными операциями являются:
#вычисление разницы между двумя моментами времени в секундах, сложение времени и
#заданного количества секунд, вычитание из времени заданного количества секунд,
#сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением до
#целой минуты).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os


class time:

    def __init__(self, hour=0, minute=0, second=0):
        hour = int(hour)
        minute = int(minute)
        second = int(second)

    def TimeToSec(self):
        self.hour= int(input('Введите часы: '))
        self.minute= int(input('Введите минуты: '))
        self.second= int(input('Введите секунды: '))

        res = (self.second + (self.minute * 60) + (self.hour * 3600))

        print(f'Перевод в секунды: {res}')
    
    def RazSec(self):
        print('Первый момент вермени')
        self.hour= int(input('Введите часы: '))
        self.minute= int(input('Введите минуты: '))
        self.second= int(input('Введите секунды: '))

        print('Второй момент вермени')
        self.hour1= int(input('Введите часы: '))
        self.minute1= int(input('Введите минуты: '))
        self.second1= int(input('Введите секунды: '))

        sec1 = (self.second + (self.minute * 60) + (self.hour * 3600))
        sec2 = (self.second1 + (self.minute1 * 60) + (self.hour1 * 3600))

        if (sec1 >= sec2):
            sec1 -= sec2
        else:
          sec1 = sec2 - sec1
        print(f'Разница времени в секундах {sec1}')

    def PerMin(self):
        self.second= int(input('Введите секунды: '))

        min = round(self.second/60)
        
        print(f'Перевод в минуты: {min}')

    def Srav(self):
        print()
        time = input("Введите первый момент времени \"час.минута.секунда\": ")
        d = time.split('.', maxsplit=2)
        time1 = datetime.timedelta(hours=int(d[0]),minutes=int(d[1]),seconds=int(d[2]))
        
        time = input("Введите вторую дату в формате \"час.минута.секунда\": ")
        d = time.split('.', maxsplit=2)
        time2 = datetime.timedelta(hours=int(d[0]),minutes=int(d[1]),seconds=int(d[2]))

        if(time1>time2):
            print(f"Время {time1} находится после времени {time2}")
           
        elif(time1<time2):
            print(f"Вермя {time1} находится до времени {time2}")
            time1,time2 = time2,time1
            
        else:
            print(f"Время {time1} равна времени {time2}")
            
    def Vich(self):
        print("Инициализация строкой ввода \"час.минута.секунда\":")
        time = input("Введите дату в формате \"час.минута.секунда\": ")
        
        d = time.split('.', maxsplit=2)

        self.hour = int(d[0])
        self.minute = int(d[1])
        self.second = int(d[2])

        time = datetime.timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)
        num = int(input("Введите целое число: "))
        time -= datetime.timedelta(seconds=num)
        
        print(f"Полсе вычитания {num} секунд время станет равной: {time} \n")

    def Sloj(self):
        print("Инициализация строкой ввода \"час.минута.секунда\":")
        time = input("Введите дату в формате \"час.минута.секунда\": ")
        
        d = time.split('.', maxsplit=2)

        self.hour = int(d[0])
        self.minute = int(d[1])
        self.second = int(d[2])

        time = datetime.timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)
        num = int(input("Введите целое число: "))
        time += datetime.timedelta(seconds=num)
        
        print(f"После сложения {num} секунд время станет равной: {time} \n")

if __name__ == '__main__':
    r1 = time()
    while True:
        os.system('cls')
        
    
        print("\nПеревести время в секунды >> [1]")
        print("Вычисление разницы >> [2]")
        print("Перевод секунд в минуты >> [3]")
        print("Сравнение двух времен >> [4]")
        print("Вычитание >> [5]")
        print("Сложение >> [6]")
        print("Выход >> [7]")
        
        command = int(input(">>"))
        
        if command == 1:
            r1.TimeToSec()
            input()    
        elif command == 2:
            r1.RazSec() 
            input() 
        elif command == 3:
            r1.PerMin()
            input() 
        elif command == 4:
            r1.Srav() 
            input() 
        elif command == 5:
            r1.Vich() 
            input() 
        elif command == 6:
            r1.Sloj() 
            input() 
        elif command == 7:
            break
        else:
            print(f"Неизветсная команда: {command}\n")
            input("Нажмите 'Enter' для продолжения")    
    #r1 = time()
    #r1.TimeToSec()

    #r1 = time()
    #r1.RazSec()

    #r1 = time()
    #r1.PerMin()

    #r1 = time()
    #r1.Srav()

    #r1 = time()
    #r1.Vich()

    #r1 = time()
    #r1.Sloj()