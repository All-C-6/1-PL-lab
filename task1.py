# -*- coding: utf-8 -*-

str1 = input("Введите два числа и желаемую операцию, чтобы получить магию: ")
str2 = str1.split(' ')
operation = True
'''
match str2[2]
case "+":
    result = str2[0] + str2[1]
case "-": 
    result = str2[0] - str2[1]
case "/":
    result = str2[0] / str2[1]
case "*":
    result = str2[0] * str2[1]
case _:
    operation = False

'''
if (str2[2] == '+'):
    result = float(str2[0]) + float(str2[1]) 
elif (str2[2] == '-'):
    result = float(str2[0]) - float(str2[1]) 
elif (str2[2] == '/'):
    result = float(str2[0]) / float(str2[1]) 
elif (str2[2] == '*'):
    result = float(str2[0]) * float(str2[1])    
else:
    operation = False
    
if operation:
    print("Результат: ", result)
else:
    print("Проверьте правильность ввода")