import random
import math
# print ('Бросок:')

#Словарь рас и расовых особенностей
races = {
        '1':{'race': 'Эльф', 'bonus' : [0, 2, -2, 2, 0, 0, 0]},
        '2':{'race': 'Гном', 'bonus' : [-2, 0, 2, 2, 0, 0, 0]},
        '3':{'race': 'Дварф', 'bonus' : [0, 0, 2, 0, 2, -2, 0]},
        '4':{'race': 'Халфлинг', 'bonus' : [-2, 2, 0, 0, 0, 2, 0]},
        '5':{'race': 'Человек', 'bonus' : [0, 0, 0, 0, 0, 0, 2]},
        '6':{'race': 'Полуэльф', 'bonus' : [0, 0, 0, 0, 0, 0, 2]},
        '7':{'race': 'Полуорк', 'bonus' : [0, 0, 0, 0, 0, 0, 2]}
        }
#Словарь классов и их костей хитов
classes = {
            '1': {'class': 'Воин', 'hit': 12},
            '2': {'class': 'Маг', 'hit': 6},
            '3': {'class': 'Плут', 'hit': 8},
            '4': {'class': 'Клирик', 'hit': 10},
}


#Функция для округления модификторов характеристик и добавление + и пробелов
def Mod(list, list2):
    for i in list:
        res = math.floor((i - 10) / 2)
        if res > 0:
            res = '+' + str(res)
        elif res == 0:
            res = ' ' + str(res)
        list2.append(res)

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

#Хуйня для вывода броска на экран
def Roll_display(x, y):
    '''
    x - количество бросков
    y - количество граней
    '''
    for i in range(x):
        roll = random.randint(1, y)
        print('\n[{}]'.format(roll))

#Функция для генерации броска на характеристику 4d6 - меньшее значение, ограничение значения характеристики не меньше восьми
def Roll_for_generation(num, list):
    for i in range(num):
        roll_list = []
        Roll(4, 6, roll_list)
        roll_list.sort()
        roll_list.pop(0)
        x = 0
        for i in roll_list:
            x += int(i)
        if x >= 8:
            list.append(x)
        else:
            rolling_list = []
            Roll_for_generation(1, rolling_list)
            x = rolling_list[0]
            list.append(x)

#Делает красиво для отображения однозначной характеристики
def K_P_A_C_U_B_O_list(list):
    for i in range (len(list)):
        if list[i] <10:
            list[i] = ' ' + str(list[i])

#Функция генерации характеристик персонажа
def Generation():
    l = []
    l2 = []
    race = ['']
    name = input('Как назвать персонажа?\n  ')
    Roll_for_generation(6, l)# генерация характеристик
    Race(l, race)# выбор расы и учет расовых бонусов к характеристикам
    Mod(l, l2)# расчет модификаторов характеристик
    K_P_A_C_U_B_O_list(l)# просто красиво
    class_choise = Class()
    class_char = classes[class_choise]['class']
    hp = classes[class_choise]['hit'] + l2[2]
    print('''
    Итак, персонаж №{} готов:

    Имя:___________{}
    Раса:__________{}
    Класс:_________{}

    ------Характеристики------
    Сила:__________[{}] | [{}]
    Ловкость:______[{}] | [{}]
    Выносливость:__[{}] | [{}]
    Интеллект:_____[{}] | [{}]
    Мудрость:______[{}] | [{}]
    Харизма:_______[{}] | [{}]
    --------------------------
    Здоровье: {}
    '''.format(num, name, races[race[0]]['race'], class_char, l[0], l2[0], l[1], l2[1], l[2], l2[2], l[3], l2[3], l[4], l2[4], l[5], l2[5], hp))



#Залупу, которая находится ниже мне в падлу подписывать, это для выбора расы
def Race_choise_bonus_choise(list, race_choise):
    race_choise_bonus_list = ['1', '2', '3', '4', '5', '6']
    choise = input()
    if choise not in race_choise_bonus_list:
        print ('Неверный выбор, попробуй еще раз.')
        Race_choise_bonus_choise(list, race_choise)
    else:
        list[int(choise) - 1] += races[race_choise]['bonus'][6]

#-----------------------------------------------------------------
def Race_choise_bonus(list, race_choise):
    print('''
    К какой характеристике прибавить бонус?
    [1] - Сила
    [2] - Ловкость
    [3] - Выносливость
    [4] - Интеллект
    [5] - Мудрость
    [6] - Харизма
    ''')
    Race_choise_bonus_choise(list, race_choise)

#-----------------------------------------------------------------
def Race_choise(list, x):
    race_list = ['1', '2', '3', '4', '5', '6', '7']
    race_choise = input()
    if race_choise not in race_list:
        print ('Неверный выбор, попробуй еще раз.')
        Race_choise(list, x)
    else:
        x[0] = race_choise
        for i in range(len(list)):
            list[i] += races[race_choise]['bonus'][i]
        if race_choise == '5' or race_choise == '6' or race_choise == '7':
            Race_choise_bonus(list, race_choise)

#-----------------------------------------------------------------
def Race(list, x):
    print('''
    Какая раса будет у персонажа?
    [1] - {}, особенности расы: +2 ЛОВ +2 ИНТ -2 ВЫН
    [2] - {}, особенности расы: +2 ВЫН +2 ИНТ -2 СИЛ
    [3] - {}, особенности расы: +2 ВЫН +2 МУД -2 ХАР
    [4] - {}, особенности расы: +2 ЛОВ +2 ХАР -2 СИЛ
    [5] - {}, особенности расы: +2 к выбранной характеристике
    [6] - {}, особенности расы: +2 к выбранной характеристике
    [7] - {}, особенности расы: +2 к выбранной характеристике
    '''.format(races['1']['race'], races['2']['race'], races['3']['race'], races['4']['race'], races['5']['race'], races['6']['race'], races['7']['race']))
    Race_choise(list, x)



def Class():
    print('''
    Какой класс будет у персонажа?
    [1] - {}, кость хитов: {}
    [2] - {}, кость хитов: {}
    [3] - {}, кость хитов: {}
    [4] - {}, кость хитов: {}
    '''.format(classes['1']['class'], 'd' + str(classes['1']['hit']), classes['2']['class'], 'd' + str(classes['2']['hit']), classes['3']['class'], 'd' + str(classes['3']['hit']), classes['4']['class'], 'd' + str(classes['4']['hit']) ))
    x = Class_choise()
    return(x)

def Class_choise():
    class_list = ['1', '2', '3', '4']
    class_choise = input()
    if class_choise not in class_list:
        print ('Неверный выбор, попробуй еще раз.')
        Class_choise()
    else:
        return(class_choise)
# roll = True
# while roll == True:
#     answ = input('\n ------- \n Бросаем?\n ------- \n')
#     if answ == 'NO':
#         roll = False
#     else:
#         d = int(input('Количество бросков: '))
#         dice = int(input('Количество граней: '))
#         Roll_display(d, dice)
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
