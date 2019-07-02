import random
import math
import json

#Словарь рас и расовых особенностей [bonus]: [str,dex,con,int,wis,cha, change_bonus] [skills]: [восприятие, дипломатия, знания, скрытность]
races = {
        '1':{'race': 'Эльф', 'bonus' : [0, 2, -2, 2, 0, 0, 0], 'skills': [2, 0, 0, 0, 0], 'speed': '6', 'size': 'средний'},
        '2':{'race': 'Гном', 'bonus' : [-2, 0, 2, 2, 0, 0, 0], 'skills': [0, 2, 0, 0, 0], 'speed': '4', 'size': 'маленький'},
        '3':{'race': 'Дварф', 'bonus' : [0, 0, 2, 0, 2, -2, 0], 'skills': [0, 0, 2, 0, 0], 'speed': '4', 'size': 'средний'},
        '4':{'race': 'Халфлинг', 'bonus' : [-2, 2, 0, 0, 0, 2, 0], 'skills': [0, 0, 0, 2, 0], 'speed': '4', 'size': 'маленький'},
        '5':{'race': 'Человек', 'bonus' : [0, 0, 0, 0, 0, 0, 2], 'skills': [0, 0, 0, 0, 2], 'speed': '6', 'size': 'средний'},
        '6':{'race': 'Полуэльф', 'bonus' : [0, 0, 0, 0, 0, 0, 2], 'skills': [0, 0, 0, 0, 2], 'speed': '6', 'size': 'средний'},
        '7':{'race': 'Полуорк', 'bonus' : [0, 0, 0, 0, 0, 0, 2], 'skills': [0, 0, 0, 0, 2], 'speed': '6', 'size': 'средний'}
        }

#Словарь классов и их костей хитов, [skills]: [восприятие, дипломатия, знания, скрытность], [бонус]: [атака, урон, защита]
classes = {
            '1': {'class': 'Воин', 'hit': 12, 'skills': [0, 0, 0, 0], 'bonus': [2, 1, 1], 'gold': 5},
            '2': {'class': 'Маг', 'hit': 6, 'skills': [1, 0, 2, 0], 'bonus': [0, 0, 1], 'gold': 3},
            '3': {'class': 'Плут', 'hit': 8, 'skills': [1, 0, 0, 1], 'bonus': [1, 1, 0], 'gold': 4},
            '4': {'class': 'Клирик', 'hit': 10, 'skills': [0, 1, 1, 0], 'bonus': [0, 0, 2], 'gold': 4},
}

#Словарь мировоззрений
alig = {
        '1':{'name': 'Законопослушный Добрый', 'short_name': 'ЗД'},
        '2':{'name': 'Законопослушный Нейтральный', 'short_name': 'ЗН'},
        '3':{'name': 'Законопослушный Злой', 'short_name': 'ЗЗ'},
        '4':{'name': 'Нейтральный Добрый', 'short_name': 'НД'},
        '5':{'name': 'Истинно Нейтральный', 'short_name': 'Н'},
        '6':{'name': 'Нейтральный Злой', 'short_name': 'НЗ'},
        '7':{'name': 'Хаотичный Добрый', 'short_name': 'ХД'},
        '8':{'name': 'Хаотичный Нейтральный', 'short_name': 'ХН'},
        '9':{'name': 'Хаотичный Злой', 'short_name': 'ХЗ'}
        }

#Словарь оружия bonus - [атака, урон, защита, здоровье, восприятие, дипломатия, знания, скрытность]
# req - воин, маг, плут, клирик, мод СИЛ, ЛОВ, ИНТ
# weapons = {
# '1': {'name': 'Кинжал', 'desc': 'Обычный кинжал, 1d4.', 'dice': [1, 4], 'req': ['0', '0', '0', '0', 0, 0, 0], 'bonus': [0, 0, 0, 0, 0, 0, 0, 0],'price': 10},
# '2': {'name': 'Короткий меч', 'desc': 'Нечто посерьезнее кухонного ножа, 1d6.', 'dice': [1, 6], 'req': ['0', '0', '0', '0', 0, 0, 0], 'bonus': [0, 0, 0, 0, 0, 0, 0, 0],'price': 25},
# '3': {'name': 'Длинный меч', 'desc': 'Выбор настоящего рыцаря, 1d8.', 'dice': [1, 8], 'req': ['0', '0', '0', '0', 0, 0, 0], 'bonus': [0, 0, 0, 0, 0, 0, 0, 0],'price': 40},
# '4': {'name': 'Посох', 'desc': 'Палка, больше подходящая для удержания равновесия, чем для боя, 1d6. Только для магов', 'dice': [1, 6], 'req': ['0', '1', '0', '0', 0, 0, 0], 'bonus': [0, 0, 0, 0, 0, 0, 0, 0],'price': 20},
# '5': {'name': 'Двуручный меч', 'desc': 'С таким не побалуешь, 2d6. Только для сильных (+3) воинов.', 'dice': [2, 6], 'req': ['1', '0', '0', '0', 3, 0, 0], 'bonus': [0, 0, 0, 0, 0, 0, 0, 0],'price': 60},
#
# }
# "2": {"name": "Короткий меч", "desc": "Нечто посерьезнее кухонного ножа, 1d6.", "dice": [1, 6], "req": ["0", "0", "0", "0", 0, 0, 0], "bonus": [0, 0, 0, 0, 0, 0, 0, 0], "price": 25},
# "3": {"name": "Длинный меч", "desc": "Выбор настоящего рыцаря, 1d8.", "dice": [1, 8], "req": ["0", "0", "0", "0", 0, 0, 0], "bonus": [0, 0, 0, 0, 0, 0, 0, 0], "price": 40},
# "4": {"name": "Посох", "desc": "Палка, больше подходящая для удержания равновесия, чем для боя, 1d6. Только для магов", "dice": [1, 6], "req": ["0", "1", "0", "0", 0, 0, 0], "bonus": [0, 0, 0, 0, 0, 0, 0, 0], "price": 20},
# "5": {"name": "Двуручный меч", "desc": "С таким не побалуешь, 2d6. Только для сильных (+3) воинов.", "dice": [2, 6], "req": ["1", "0", "0", "0", 3, 0, 0], "bonus": [0, 0, 0, 0, 0, 0, 0, 0], "price": 60},

# with open("weapon.json", "w", encoding='utf-8') as write_file:
#     json.dump(weapons, write_file, ensure_ascii=False, indent=4)

with open("weapons.json", "r", encoding='utf-8-sig') as w:
    weapons = json.load(w)
with open("armor.json", "r", encoding='utf-8-sig') as a:
    armors = json.load(a)
with open("equip.json", "r", encoding='utf-8-sig') as e:
    equip = json.load(e)
#print(json.dumps(data, indent=4, ensure_ascii=False, separators=(',', ': ')))
# for i in range (1, len(data)):
#     print (data[str(i)]['name'])
#     print (data[str(i)]['desc'])
#     print ('')

#Словарь доспехов bonus - [атака, урон, защита, здоровье, восприятие, дипломатия, знания, скрытность]
# req - воин, маг, плут, клирик, мод СИЛ, ЛОВ, ИНТ
# armors = {
# '1': {'name': 'Тканый доспех', 'desc': 'Какая-никакая, а все же защита. +1 к защите.', 'req': ['0', '0', '0', '0', 0, 0, 0], 'bonus': [0, 0, 1, 0, 0, 0, 0, 0], 'price': 10},
# '2': {'name': 'Стеганый доспех', 'desc': 'Уже нечто лучшее. +2 к защите. Требования: [ЛОВ] +1', 'req': ['0', '0', '0', '0', 0, 1, 0], 'bonus': [0, 0, 2, 0, 0, 0, 0, 0], 'price': 30},
# '3': {'name': 'Кожанный доспех', 'desc': 'Удобный доспех для скрытных личностей. +3 к защите, +1 к скрытности. Требования: класс - плут или [ЛОВ] +2', 'req': ['0', '0', '1', '0', 0, 2, 0], 'bonus': [0, 0, 3, 0, 0, 0, 0, 1], 'price': 70},
# '4': {'name': 'Кольчуга', 'desc': 'Прочный повседневный доспех. +3 к защите. Требования: класс - воин или [СИЛ] +1', 'req': ['1', '0', '0', '0', 1, 0, 0], 'bonus': [0, 0, 3, 0, 0, 0, 0, 1], 'price': 60},
# '5': {'name': 'Пластинчатый доспех', 'desc': 'В таком и дракон не страшен. +5 к защите. Требования: класс - воин или [СИЛ] +3', 'req': ['1', '0', '0', '0', 3, 0, 0], 'bonus': [0, 0, 5, 0, 0, 0, 0, 1], 'price': 100}
#
# }
#
# #Словарь прочего снаряжения type - 1 зелья лечения, 2 зелья гранаты, 3 яды, 4 свитки баф, 5 свитки урона, 6 руны - пассив улучшения req - воин, маг, плут, клирик, воспр, дипл, знан, скрыт
# equipments = {
# '1': {'name': 'Малое зелье лечения', 'desc': 'Восстанавливает 1d4 + мод. ВЫН здоровья.', 'type': '1', 'req': ['0', '0', '0', '0', 0, 0, 0, 0], 'dice': [1, 4], 'price': 15},
# '2': {'name': 'Среднее зелье лечения', 'desc': 'Восстанавливает 1d6 + мод. ВЫН здоровья.', 'type': '1', 'req': ['0', '0', '0', '0', 0, 0, 0, 0], 'dice': [1, 6], 'price': 30},
# '3': {'name': 'Крысиный яд', 'desc': 'Наносит дополнительно 2 единицы урона на 3 попадания. Требования: класс - плут, или навык скрытность +2', 'type': '3', 'req': ['0', '0', '1', '0', 0, 0, 0, 2], 'dmg_type': [1, 1, 1, 0, 1], 'bonus': [2, 3], 'price': 20},
# '4': {'name': 'Бутылек святой воды', 'desc': 'Наносит 2d6 урона, работает только с нежитью.', 'type': '2', 'req': ['0', '0', '0', '0', 0, 0, 0, 0], 'dmg_type': [0, 0, 0, 1, 1], 'dice': [2, 6], 'price': 10},
# '5': {'name': 'Алхимический огонь', 'desc': 'Наносит 1d6 урона огнем.', 'type': '2', 'req': ['0', '0', '0', '0', 0, 0, 0, 0], 'dmg_type': [1, 1, 1, 1, 0], 'dice': [1, 6], 'price': 20},
# '6': {'name': 'Свиток огненной стрелы', 'desc': 'Наносит 2d6 урона. Требования: класс - маг, или навык знания +2.', 'type': '5', 'req': ['0', '0', '0', '1', 0, 0, 2, 0], 'dmg_type': [1, 1, 1, 1, 0], 'dice': [2, 6], 'price': 20},
# '7': {'name': 'Свиток бычьего здоровья', 'desc': 'Увеличивает количество максимального здоровья на 3, работает сутки. Требования: класс - маг, или навык знания +2.', 'type': '4', 'req': ['0', '0', '0', '1', 0, 0, 2, 0], 'bonus': 3, 'price': 25},
# '8': {'name': 'Свиток каменной кожи', 'desc': 'Увеличивает защиту на 3, работает сутки. Требования: класс - маг, или навык знания +2.', 'type': '4', 'req': ['0', '0', '0', '1', 0, 0, 2, 0], 'bonus': 3, 'price': 30},
#
# }

towns = ['Болотные Крыши', 'Путевой', 'Лесной Оазис', 'Озерный', 'Междулесец', 'Когдаград']

town = towns[random.randint(0, len(towns) - 1)]

def Town():
    print('''
    -----------------------------------------------------
      Ты находишься в городишке под названием {}.
      Можно пойти:
    -----------------------------------------------------
    [1] - магазин
    [2] - таверна
    [3] - доска объявлений
    [4] - выйти из города
    ----------------------
    [5] - посмотреть снаряжение и характеристики
    '''.format(town))
    current_place[0] = place_list[0]
    Town_go()

def Town_go():
    towngo_list = ['1', '2', '3', '4', '5']
    towngo_choise = input()
    if towngo_choise not in towngo_list:
        print ('Неверный выбор, попробуй еще раз.')
        Town_go()
    else:
        if towngo_choise == '1':
            Shop()
        elif towngo_choise == '2':
            Tawern()
        elif towngo_choise == '3':
            Board()
        elif towngo_choise == '4':
            Town_quit()
        elif towngo_choise == '5':
            Inventory()

def Shop():
    print('''
    -----------------------------------------------------
      Ты входишь в местную лавку. Тут куча разных товаров.
      В какой отдел идем?
    -----------------------------------------------------
    [1] - "Средства по убиению"
    [2] - "Средства по защите от убиения"
    [3] - "Разные средства"
    [4] - уходим отсюда
    ----------------------
    [5] - посмотреть снаряжение и характеристики
    ''')
    current_place[0] = place_list[2]
    Shop_cat()

def Shop_cat():
    cat_list = ['1', '2', '3', '4', '5']
    cat_choise = input()
    if cat_choise not in cat_list:
        print ('Неверный выбор, попробуй еще раз.')
        Shop_cat()
    else:
        if cat_choise == '4':
            Town()
        elif cat_choise == '5':
            Inventory()
        else:
            Shop_buy(cat_choise)

def Shop_buy(x):
    dict = {}
    list = {}
    if x == '1':
        print('''
    -----------------------------------------------------
      Ты проходишь в комнату, где расположились разные клинки и оружие.
    -----------------------------------------------------''')
        dict = weapons
        list = inventory_weapon
    elif x == '2':
        print('''
    -----------------------------------------------------
      Ты заходишь в помещение, где тебя встречают манекены одетые в разные доспехи.
    -----------------------------------------------------''')
        dict = armors
        list = inventory_armor
    else:
        print('''
    -----------------------------------------------------
      Ты пришел в забитую прозрачными витринами комнату.
      Видно, как содержимое склянок переливается разными цветами.
    -----------------------------------------------------''')
        dict = equip
        list = inventory_equip
    print('''
    У тебя есть {} золотых.

    Торговец предлагает тебе:'''.format(gold[0]))
    for i in range(1, len(dict)):
        print('''
    [{}] - {}
    {} {}
    Стоимость: {} золотых
        '''.format(i, dict[str(i)]['name'], dict[str(i)]['desc'], dict[str(i)]['dop_desc'], dict[str(i)]['price']))
    print('''
    [-] - вернуться обратно''')
    Shop_buy_choise(dict, list)

def Shop_buy_choise(dict, list):
    buy_list = ['-']
    for i in range(1, len(dict)):
        buy_list.append(str(i))
    buy_choise = input()
    if buy_choise not in buy_list:
        print ('Неверный выбор, попробуй еще раз.')
        Shop_buy_choise(dict)
    elif buy_choise == '-':
        print('''
    -----------------------------------------------------
      Ты выходишь обратно в холл.
    -----------------------------------------------------''')
        Shop()
    else:
        if gold[0] >= dict[buy_choise]['price']:
            gold[0] -= dict[buy_choise]['price']
            if buy_choise in list:
                list[buy_choise]['num'] +=1
            else:
                list[buy_choise] = {'name': dict[buy_choise]['name'], 'num': 1, 'desc':  dict[buy_choise]['desc'], 'id': buy_choise}
            print('''
    -----------------------------------------------------
      Лавочник отдает тебе [{}], забирая кошель с {} монетами.
        - Спасибо за покупку.

      У тебя осталось {} золотых.
    -----------------------------------------------------
'''.format(dict[buy_choise]['name'].lower(), dict[buy_choise]['price'], gold[0]))
        Shop()

def Inventory():
    print('''
    -----------------------------------------------------
      Ты садишься возле своего рюкзака.

      На тебе [{}].
      В руках ты держишь [{}].
      На поясе висит мешочек с [{}] золота.
    -----------------------------------------------------
    [1] - посмотреть снаряжение в рюкзаке
    [2] - поменять надетое снаряжение
    [3] - посмотреть листок со своими характеристиками
    [4] - заглянуть в дневник с заданием
    [5] - пойти дальше
'''.format(active_armor[0], active_weapon[0], gold[0]))
    Inventory_choise()

def Inventory_choise():
    inv_list = ['1', '2', '3', '4', '5']
    inv_choise = input()
    if inv_choise not in inv_list:
        print ('Неверный выбор, попробуй еще раз.')
        Inventory_choise()
    else:
        if inv_choise == '5':
            Inventory_quit()
        else:
            Inventory_choise_second(inv_choise)

def Inventory_choise_second(x):
    if x == '1':
        print('''
    -----------------------------------------------------
      У тебя в рюкзаке:

    ------------
      Оружие:
    ------------''')
        for i in inventory_weapon:
            print('''
        {} - {} шт.
        {}'''.format(inventory_weapon[i]['name'], inventory_weapon[i]['num'], inventory_weapon[i]['desc']))
        print('''
    ------------
      Доспехи:
    ------------''')
        for i in inventory_armor:
            print('''
        {} - {} шт.
        {}'''.format(inventory_armor[i]['name'], inventory_armor[i]['num'], inventory_armor[i]['desc']))
        print('''
    ------------
      Прочее:
    ------------''')
        for i in inventory_equip:
            print('''
        {} - {} шт.
        {}'''.format(inventory_equip[i]['name'], inventory_equip[i]['num'], inventory_equip[i]['desc']))
        print('    -----------------------------------------------------')
        Inventory()
    if x == '2':
        print('''
    [1] - оружие
    [2] - доспех
    [3] - назад''')
        Inventory_swich_gear()

def Inventory_swich_gear():
    num = 1
    inv_list = ['1', '2', '3']
    inv_choise = input()
    if inv_choise not in inv_list:
        print ('Неверный выбор, попробуй еще раз.')
        Inventory_swich_gear()
    else:
        if inv_choise == '3':
            Inventory()
        elif inv_choise == '1':
            swich_list = active_weapon
            list = inventory_weapon
            print('''
      Текущее оружие: {}
    -----------------------------------------------------
      Доступное оружие:
    -----------------------------------------------------'''.format(swich_list[0]))
            for i in list:
                print('''
        [{}] - {} - {} шт.
        {}'''.format(num, list[i]['name'], list[i]['num'], list[i]['desc']))
                num +=1
            print('''
        [-] - назад
    -----------------------------------------------------
      Какой выбрать?
    -----------------------------------------------------''')
            Inventory_swich_gear_choise(swich_list, list)
        elif inv_choise == '2':
            swich_list = active_armor
            list = inventory_armor
            print('''
      Текущий доспех: {}
    -----------------------------------------------------
      Доступные доспехи:
    -----------------------------------------------------'''.format(swich_list[0]))
            for i in list:
                print('''
        [{}] - {} - {} шт.
        {}'''.format(num, list[i]['name'], list[i]['num'], list[i]['desc']))
                num +=1
            print('''
        [-] - назад
    -----------------------------------------------------
      Какой выбрать?
    -----------------------------------------------------''')
            Inventory_swich_gear_choise(swich_list, list)

def Inventory_swich_gear_choise(list, list_2):
    choise_list = ['-']
    for i in range(1, len(list_2)+1):
        choise_list.append(str(i))
    swich_choise = input()
    if swich_choise not in choise_list:
        print ('Неверный выбор, попробуй еще раз.')
        Inventory_swich_gear_choise(list, list_2)
    else:
        list[0] = list_2[int(swich_choise)-1]['name']
#Функция для генерации х бросков y-гранного кубика, результат записывается в список
def Roll(x, y, list):
    for i in range(x):
        roll = random.randint(1, y)
        list.append(roll)


#Хуйня для вывода броска на экран
def Roll_display(x, y):
    for i in range(x):
        roll = random.randint(1, y)
        print('\n[{}]'.format(roll))


#Функция генерации характеристик персонажа
def Generation():
    l = []
    l2 = []
    l_skill = [0, 0, 0, 0]
    race = ['']
    align = ['']
    class_ch = ['', '', '', '', '', '', '']
    name = input('Как назвать персонажа?\n  ')
    Roll_for_generation(6, l) # генерация характеристик
    Race(l, race) # выбор расы и учет расовых бонусов к характеристикам
    Mod(l, l2) # расчет модификаторов характеристик
    K_P_A_C_U_B_O_list(l) # просто красиво
    Alignment(align) # выбор мировоззрения
    Class(class_ch, l2) # выбор класса
    Skills(l_skill, l2, race, class_ch) # считает скиллы
    gold = Roll_gold(class_ch[6]) # начальное золото
    print('''
    Итак, персонаж №{} готов:

    Имя:_____________{}
    Раса:____________{}
    Класс:___________{}
    Мировоззрение:___{}'''.format(num, name, races[race[0]]['race'], class_ch[1], alig[align[0]]['short_name']))
    print('''
    ------Характеристики------
    Сила:__________[{}] | [{}]
    Ловкость:______[{}] | [{}]
    Выносливость:__[{}] | [{}]
    Интеллект:_____[{}] | [{}]
    Мудрость:______[{}] | [{}]
    Харизма:_______[{}] | [{}]
    --------------------------'''.format(l[0], l2[0], l[1], l2[1], l[2], l2[2], l[3], l2[3], l[4], l2[4], l[5], l2[5]))
    print('''
    Здоровье: {}
    Бонус к атаке: {}
    Бонус к урону: {}
    Бонус к защите: {}

    Скорость: {}
    Размер: {}'''.format(class_ch[2], class_ch[3], class_ch[4], class_ch[5], races[race[0]]['speed'], races[race[0]]['size']))
    print('''
    -----Навыки-----
    Восприятие: [{}]
    Дипломатия: [{}]
    Знания:     [{}]
    Скрытность: [{}]
    ----------------'''.format(l_skill[0], l_skill[1], l_skill[2], l_skill[3]))
    print('''
    Золото: {} '''.format(gold))



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
    [1] - {}, особенности расы: +2 ЛОВ +2 ИНТ -2 ВЫН, +2 восприятие
    [2] - {}, особенности расы: +2 ВЫН +2 ИНТ -2 СИЛ, +2 дипломатия
    [3] - {}, особенности расы: +2 ВЫН +2 МУД -2 ХАР, +2 знания
    [4] - {}, особенности расы: +2 ЛОВ +2 ХАР -2 СИЛ, +2 скрытность
    [5] - {}, особенности расы: +2 к выбранной характеристике, +2 к выбранному навыку
    [6] - {}, особенности расы: +2 к выбранной характеристике, +2 к выбранному навыку
    [7] - {}, особенности расы: +2 к выбранной характеристике, +2 к выбранному навыку
    '''.format(races['1']['race'], races['2']['race'], races['3']['race'], races['4']['race'], races['5']['race'], races['6']['race'], races['7']['race']))
    Race_choise(list, x)


# Хуйня для выбора класса
def Class(x, list):
    print('''
    Какой класс будет у персонажа?
    [1] - {}, кость хитов: {},
        навыки: восприятие +0, дипломатия +0, знания +0, скрытность +0
        бой: атака +2, урон +1, защита +1
        начальное золото 5d6*10

    [2] - {}, кость хитов: {}
        навыки: восприятие +1, дипломатия +0, знания +2, скрытность +0
        бой: атака +0, урон +0, защита +1
        начальное золото 3d6*10

    [3] - {}, кость хитов: {}
        навыки: восприятие +1, дипломатия +0, знания +0, скрытность +1
        бой: атака +1, урон +1, защита +0
        начальное золото 4d6*10

    [4] - {}, кость хитов: {}
        навыки: восприятие +0, дипломатия +1, знания +1, скрытность +0
        бой: атака +0, урон +0, защита +2
        начальное золото 4d6*10
    '''.format(classes['1']['class'], 'd' + str(classes['1']['hit']), classes['2']['class'], 'd' + str(classes['2']['hit']), classes['3']['class'], 'd' + str(classes['3']['hit']), classes['4']['class'], 'd' + str(classes['4']['hit']) ))
    Class_choise(x, list)

#-----------------------------------------------------------------
def Class_choise(x, list):
    class_list = ['1', '2', '3', '4']
    class_choise = input()
    if class_choise not in class_list:
        print ('Неверный выбор, попробуй еще раз.')
        Class_choise(x, list)
    else:
        x[0] = class_choise
        x[1] = classes[class_choise]['class']
        x[2] = int(classes[class_choise]['hit']) + int(list[2])
        x[3] = int(classes[class_choise]['bonus'][0])
        x[4] = int(classes[class_choise]['bonus'][1]) + int(list[0])
        x[5] = int(classes[class_choise]['bonus'][2]) + int(list[1])
        x[6] = classes[class_choise]['gold']


#Хуйня для выбора мировоззрения персонажа, пока хз, куда его прикрутить, вероятно оно нахуй не нужно
def Alignment(x):
        print ('''
        Какое мировоззрение будет у персонажа?

        [1. {}]         [4. {}]     [7. {}]
        [2. {}]    [5. {}]    [8. {}]
        [3. {}]           [6. {}]       [9. {}]
        '''.format(alig['1']['name'], alig['4']['name'], alig['7']['name'], alig['2']['name'], alig['5']['name'], alig['8']['name'], alig['3']['name'], alig['6']['name'], alig['9']['name']))
        Alignment_choise(x)

#-----------------------------------------------------------------
def Alignment_choise(x):
    alig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    alig_choise = input()
    if alig_choise not in alig_list:
        print ('Неверный выбор, попробуй еще раз.')
        Alignment_choise(x)
    else:
        x[0] = alig_choise


#хуйня для выбора бонуса к скиллу у полурас
def Skills_choise_bonus(list, x):
    skills_bonus_list = ['1', '2', '3', '4']
    choise = input()
    if choise not in skills_bonus_list:
        print ('Неверный выбор, попробуй еще раз.')
        Skills_choise_bonus(list, x)
    else:
        list[int(choise) - 1] += races[x[0]]['skills'][4]

#---------------------------------------------
def Skills_choise(list, x):
    print('''
    К какому навыку прибавить бонус?
    [1] - Восприятие
    [2] - Дипломатия
    [3] - Знания
    [4] - Скрытность
    ''')
    Skills_choise_bonus(list, x)


#хуйня для скиллов прибавляет к навыкам бонусы расы, класса и модификаторов характеристик, отвечающих за навыки
def Skills (list, list_2, x, x2):
    list[0] += int(list_2[4])
    list[1] += int(list_2[5])
    list[2] += int(list_2[3])
    list[3] += int(list_2[1])
    for i in range(len(list)):
        list[i] = list[i] + races[x[0]]['skills'][i] + classes[x2[0]]['skills'][i]
    if x[0] == '5' or x[0] == '6' or x[0] == '7':
        Skills_choise(list, x)
    if races[x[0]]['size'] == 'маленький':
        list[3] += 2
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = '+' + str(list[i])
        if list[i] == 0:
            list[i] = ' ' + str(list[i])


#Функция для округления модификторов характеристик и добавление + и пробелов
def Mod(list, list2):
    for i in list:
        res = math.floor((i - 10) / 2)
        if res > 0:
            res = '+' + str(res)
        elif res == 0:
            res = ' ' + str(res)
        list2.append(res)


#Ролл начального золота
def Roll_gold(x):
    list = []
    y = 0
    for i in range(int(x)):
        roll = random.randint(1, 6)
        list.append(roll)
    for i in range(len(list)):
        y += int(list[i])
    y = y*10
    return (y)


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


#-----------------------------------------------------------------

#Счетчик персонажей и цикл бесконечного создания
# num = 1
# go = True
# while go == True:
#     answ = input('\n -------------------------------- \nГенерируем? Если нет, напиши "НЕТ"\n -------------------------------- \n')
#     if answ == 'НЕТ':
#         go = False
#     else:
#         Generation()
#         num+=1
place_list = ['Town', 'Tawern', 'Shop', 'Road', 'Forest', 'Cave', 'Ruin']
current_place = [0]
gold = [0]
inventory_weapon = {'0': {'name': 'Камень', 'num': 1, 'desc': 'Простой камень, в чем-то заляпан.[0]', 'id': '0'}}
inventory_armor = {'0': {'name': 'Рубаха и штаны', 'num': 1, 'desc': 'Простецкий наряд, вероятно, его кто-то уже носил. + 0 к защите', 'id': '0'}}
inventory_equip = {}
active_weapon = [inventory_weapon['0']['name'].lower()]
active_armor = [inventory_armor['0']['name'].lower()]
gold[0] = Roll_gold(10)
print(inventory_weapon[0])
Town()
