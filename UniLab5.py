# -*- coding: cp1251 -*-

import random

while True:
    
    checker = False
    primaryChoice = input("����� ������� ��� �������� : \n1)\n2)\n3)\n4)\n5) - �����\n����� : ")
    if [num for num in primaryChoice if num not in ".,/*-+1234567890"]: checker = True
    if checker == True:
        print("��� ������")
        break
    primaryChoice = int(primaryChoice)
    
    if primaryChoice == 1:
        mistahFlag = 0
        ListOfNumbers = list()
        humanAnswer = input("������ ����� �� 0 �� 15 : ")
        humanAnswer = int(humanAnswer)
        for i in range(5):
            Num = random.randint(0, 15)
            if humanAnswer == Num: 
                mistahFlag = mistahFlag + 1
            ListOfNumbers.append(Num)
        if mistahFlag > 0: 
            print("�� ������ �����, ��� ���� ������ �����")
        else:
            print("��� ������ �����, ��� ���� ������ �����")
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
            print("������������� ����� ���")

    if primaryChoice == 3:
        dayOfWeek = ("�����������", "�������", "�������", "�������", "�����", "�������", "�����������")
        employee = input("������� ������ �������� � ������ ? ")
        employee = int(employee)
        WeekEnds = dayOfWeek[:employee]
        WeekWork = dayOfWeek[employee:]
        print("�������� : ", WeekEnds, " ������� ��� : ", WeekWork)
        
    if primaryChoice == 4:
        myClass = ["������", "������", "�������", "������", "�������", "�������", "������", "�������", "�������", "��������"]
        otherClass = ["�������", "��������", "��������", "������", "������", "�������", "�������", "����������", "��������", "��������"]
        sportClub = list()
        for i in range(5):
            choicer = random.randint(0,1)
            if choicer == 0:
                howMucher = random.randint(0,10)
                sportClub.append(myClass[howMucher])
            if choicer == 1:
                howMucher = random.randint(0,10)
                sportClub.append(otherClass[howMucher])
        print("������ ���������� : ", sportClub, " ����� ������ : ", len(sportClub))
        print("�������� ������ ����� : ", myClass, otherClass)
        sportClub = sorted(sportClub)
        print("������������� ������ ���������� : ", sportClub)
        ivanovPow = 0
        for i in range(5):
            if "������" == sportClub[i]:
                ivanovPow = ivanovPow + 1
        print("������ ����������� � ������ ���������� : ", ivanovPow)
        
    if primaryChoice == 5: 
            break