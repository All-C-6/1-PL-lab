# -*- coding: utf-8 -*-

str2 = input("Введите два числа и желаемую операцию, чтобы получить магию: ").split(' ')

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
def calc(str1):
    try:
        if (float(str1[1]) == 0.0):
            return " "
        elif ((str1[2] == '+')):
            result = float(str1[0]) + float(str1[1]) 
            return result
        elif ((str1[2] == '-')):
            result = float(str1[0]) - float(str1[1]) 
            return result
        elif ((str1[2] == '/')):
            result = float(str1[0]) / float(str1[1]) 
            return result
        elif ((str1[2] == '*')):
            result = float(str1[0]) * float(str1[1])
            return result
        else:
            return " "
    except ValueError:
        return " "
    
if (calc(str2) == " "):
    print("Проверьте правильность ввода")
else:
    print("Результат: ", calc(str2))
    