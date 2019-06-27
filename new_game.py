import random
import math
print ('Привет, давай сгенерируем персонажа')

#Функция для округления модификторов характеристик и добавление + и пробелов
def rd(x):
    res = math.floor((x - 10) / 2)
    if res > 0:
        res = '+' + str(res)
    elif res == 0:
        res = ' ' + str(res)
    return(res)

#Функция для генерации х бросков y-гранного кубика, результат записывается в список
def Roll(x, y, list):
    '''
    x - количество бросков
    y - количество граней
    list - список, куда будут записаны значения
    '''
    for i in range(x):
        roll = random.randint(1, y)
        list.append(roll)

#Функция для генерации броска на характеристику 4d6 - меньшее значение, ограничение значения характеристики не меньше восьми
def Roll_for_generation():
    list = []
    Roll(4, 6, list)
    list.sort()
    list.pop(0)
    x = 0
    for i in list:
        x += int(i)
    if x >= 8:
        return (x)
    else:
        x = Roll_for_generation()
        return(x)

#Делает красиво для отображения однозначной характеристики
def K_P_A_C_U_B_O_list(list):
    for i in range (len(list)):
        if list[i] <10:
            list[i] = ' ' + str(list[i])

#Функция генерации характеристик персонажа
def Generation():
    l = []
    l2 = []
    for i in range (6):
        x = Roll_for_generation()
        l.append(x)
        l2.append(x)
    K_P_A_C_U_B_O_list(l2)
    print('''Итак, персонаж №{} готов:
    Сила:__________[{}] | [{}]
    Ловкость:______[{}] | [{}]
    Выносливость:__[{}] | [{}]
    Интеллект:_____[{}] | [{}]
    Мудрость:______[{}] | [{}]
    Харизма:_______[{}] | [{}]
    '''.format(num, l2[0], rd(l[0]), l2[1], rd(l[1]), l2[2], rd(l[2]), l2[3], rd(l[3]), l2[4], rd(l[4]), l2[5], rd(l[5])))



#Счетчик персонажей и цикл бесконечного создания
num = 1
go = True
while go == True:
    answ = input('\n -------------------------------- \nГенерируем? Если нет, напиши "НЕТ"\n -------------------------------- \n')
    if answ == 'НЕТ':
        go = False
    else:
        Generation()
        num+=1
