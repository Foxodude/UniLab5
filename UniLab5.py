# -*- coding: cp1251 -*-

import random

while True:
    
    checker = False
    primaryChoice = input("Выбор задания для проверки : \n1)\n2)\n3)\n4)\n5) - Выход\nВыбор : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("Так нельзя")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        mistahFlag = 0
        ListOfNumbers = list()
        humanAnswer = input("Угадай число от 0 до 15 : ")
        humanAnswer = int(humanAnswer)
        for i in range(5):
            Num = random.randint(0, 15)
            if humanAnswer == Num: 
                mistahFlag = mistahFlag + 1
            ListOfNumbers.append(Num)
        if mistahFlag > 0: 
            print("Ты угадал число, вот весь список чисел")
        else:
            print("нет такого числа, вот весь список чисел")
        print(ListOfNumbers)
        
    if primaryChoice == 2:
        ListOfNumbers = list()
        randRange = random.randint(0, 15)
        for i in range(randRange):
            Num = random.randint(0, 100)
            ListOfNumbers.append(Num)
        
        ListOfChaos = list()
        for i in range(randRange):
            x = ListOfNumbers[i]
            j = i + 1
            for j in range(i + 1, randRange):
               y = ListOfNumbers[j]
               if x == y:
                   ListOfChaos.append(x)
        if len(ListOfChaos) != 0:
            print(ListOfChaos)
        else:
            print("повторяющихся чисел нет")

    if primaryChoice == 3:
        dayOfWeek = ("Воскресенье", "Суббота", "Пятница", "Четверг", "Среда", "Вторник", "Понедельник")
        employee = input("Сколько хотите выходных в неделю ? ")
        employee = int(employee)
        WeekEnds = dayOfWeek[:employee]
        WeekWork = dayOfWeek[employee:]
        print("Выходные : ", WeekEnds, " Рабочие дни : ", WeekWork)
        
    if primaryChoice == 4:
        myClass = ["Иванов", "Петров", "Сидоров", "Козлов", "Новиков", "Морозов", "Волков", "Лебедев", "Смирнов", "Кузнецов"]
        otherClass = ["Федоров", "Соловьев", "Васильев", "Зайцев", "Павлов", "Семенов", "Голубев", "Виноградов", "Богданов", "Воробьев"]
        sportClub = list()
        for i in range(5):
            choicer = random.randint(0,1)
            if choicer == 0:
                howMucher = random.randint(0,10)
                sportClub.append(myClass[howMucher])
            if choicer == 1:
                howMucher = random.randint(0,10)
                sportClub.append(otherClass[howMucher])
        print("Список спортивный : ", sportClub, " длина списка : ", len(sportClub))
        print("Исходные списки групп : ", myClass, otherClass)
        sportClub = sorted(sportClub)
        print("Сортированный список спортивных : ", sportClub)
        ivanovPow = 0
        for i in range(5):
            if "Иванов" == sportClub[i]:
                ivanovPow = ivanovPow + 1
        print("Иванов встречается в списке спортивных : ", ivanovPow)
        
    if primaryChoice == 5: 
            break
