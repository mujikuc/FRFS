from random import randint
#Вся залупа держится на if else и циклах, ничего хорошего ниже ты не увидишь
print ('Fantasy Road Fighter Simulator v.0.001')
print ('\nПривет, друг. Тебе предстоит опасное путешествие, полное врагов, убийств и зелий.\nЭто хардкорная игра, не прощающая ошибок. Будь внимателен.')
#Ниже прописаны переменные, которые будут задаваться позже
hp = 0
dmg = 0
min_dmg = 0
max_dmg = 0
hero_class_name = 'класс'
potion_count = 0 #Счетчик зелий
kill_count = 0 #Счетчик убийств
exp_count = 0 #Счетчик опыта - это очки
#Еще можно добавить золото, выпадающее в диапазоне, которое будет чем то вроде "очков"
#Зелья, кстати, приклеины криво и могут восстанавливать хп больше, чем изначальное, мне в падлу ставить на это чек на характеристики класса из словаря

#Вот эту хуйню надо приписюнить к sqlite, мне в падлу
#Ниже словарь с оружием под класс персонажа
weapons = { 1: {'min_dmg': 1, 'max_dmg': 10}, 2:{'min_dmg': 2, 'max_dmg': 8}, 3:{'min_dmg': 1, 'max_dmg': 8}, 4:{'min_dmg': 1, 'max_dmg': 2}}

#Ниже словарь с противниками
enemies = {1:{'name': 'Бандит', 'hp': 10, 'min_dmg': 1, 'max_dmg': 4, 'exp': 4}, 2:{'name': 'Орк', 'hp': 15, 'min_dmg': 1, 'max_dmg': 8, 'exp': 10}, 3:{'name': 'Волк', 'hp': 8, 'min_dmg': 2, 'max_dmg': 6, 'exp': 6}}


# , способность: Колючий доспех (половина урона отражается противнику)
reflect_value = 0
reflect = ''
# , способность: Меткий удар (25% нанести х2 урона)
chance_crit = 0
crit = ''

# , способность: Магический барьер (40% уклониться от урона)
chance_evade = 0
evade = ''
#Ниже задается имя персонажа игрока и его класс. Нужно доработать способности класса
name = input ('\nДля начала скажи, как тебя зовут: ')
hero_class = input ('''
А теперь, {}, выбери свой класс:
[1] Воин - здоровье: 20, оружие: секира 1d10, способность: Колючий доспех (Отражение 50% полученного урона)
[2] Убийца - здоровье: 15, оружие: два кинжала 1d4, способность: Меткий удар (Шанс 25% на нанесение двойного урона)
[3] Маг - здоровье: 10, оружие: посох 1d8, способность: Магический барьер (Шанс 50% на уклонение от атаки)

'''.format(name))
if hero_class == '1':
    hero_class_name = 'воин'
    hp = 20
    weapon = 'секира 1d10'
    min_dmg = weapons[int(hero_class)]['min_dmg']
    max_dmg = weapons[int(hero_class)]['max_dmg']
    skill = 'Колючий доспех (Отражение 50% полученного урона, округление в меньшую сторону)'
elif hero_class == '2':
    hero_class_name = 'убийца'
    hp = 15
    weapon = 'два кинжала 1d4'
    min_dmg = weapons[int(hero_class)]['min_dmg']
    max_dmg = weapons[int(hero_class)]['max_dmg']
    skill = 'Меткий удар (Шанс 25% на нанесение двойного урона)'
elif hero_class == '3':
    hero_class_name = 'маг'
    hp = 10
    weapon = 'посох 1d8'
    min_dmg = weapons[int(hero_class)]['min_dmg']
    max_dmg = weapons[int(hero_class)]['max_dmg']
    skill = 'Магический барьер (Шанс 50% на уклонение от атаки)'
else:
    print ('\nЧувак, ты облажался.')
    hero_class_name = 'непонятно что'
    hp = 1
    weapon = 'ручки 1d2'
    min_dmg = weapons[4]['min_dmg']
    max_dmg = weapons[4]['max_dmg']
    skill = 'ты вонючка'

#Ниже отображаются параметры класса, выбранного игроком и имя персонажа
print ('''
Теперь ты {} по имени {}.
Твои характеристики:
   - Здоровье: {}
   - Оружие: {}
   - Способность: {}
   '''.format(hero_class_name, name, hp, weapon, skill))

#А тут начинается жопа
choise = input ('Ну что, пора бы уже отправиться в путь. Ты согласен?\n[1] - Да, вперед\n[2] - Нет, подожди\n')
if choise == '1' or choise == '':
    print ('\nПоихали.\n')
    go = True
    while go == True: #Типа пока мы идем, мы встречаем противников и деремся с ними
        fight = True
        print ('\n ----------------------- \nТы движешься вперед по дороге, но вдруг что-то замечаешь.')
        #Блок ниже помещен сюда, чтобы при каждой итерации цикла появлялся новый противник
        en_key = randint(1, len(enemies)) #Случайный выбор из словаря с противниками
        #Характеристики противника, которые заполняются из словаря по ключу en_key
        en = enemies[en_key]['name']
        en_hp = enemies[en_key]['hp']
        en_min_dmg = enemies[en_key]['min_dmg']
        en_max_dmg = enemies[en_key]['max_dmg']
        add_exp = enemies[en_key]['exp']
        # print (len(enemies)) #Длина словаря с характеристиками противника
        # print (en) #Имя выбранного противника

        while fight == True: #Вот тут цикл для боя
            print ('Перед тобой стоит {}, у него {} здоровья.'.format(en.lower(), en_hp)) #Вот эти вот ".ловер" заменяет все буквы переменной на прописные
            action = input ('''У тебя {} здоровья. Что делаем?
            [1] - бьем {}
            [2] - пропускаем ход
            [3] - выпить зелье лечения ({} шт.)

            '''.format(hp, en.lower() + 'а', potion_count))
            if action == '1' or action == '': #Если бьем, то нанесем урон противнику, а потом получим сами
                dmg = randint(min_dmg, max_dmg)
                en_dmg = randint(en_min_dmg, en_max_dmg)
                #Способность убийцы на 25% шанс крита
                if hero_class == '2':
                    chance_crit = randint(1, 100)
                    if chance_crit >= 75:
                        dmg *= 2
                        crit = 'критического ' #Дописывается к отображению нанесенного урона
                    else:
                        crit = ''
                #Способность воина на 50% отражение
                if hero_class == '1':
                    reflect_value = int(en_dmg/2)
                    reflect = ' и получил в ответ {} урона'.format(reflect_value)
                #Способность мага на 50% уклонение
                if hero_class == '3':
                    chance_evade = randint(1, 100)
                    if chance_evade >= 50:
                        en_dmg = 0
                        evade = 'промахнулся и ' #Дописывается к отображению полученного урона
                    else:
                        evade = ''
                en_hp -= dmg
                print ('\n ----------------------- \n Ты нанес {} {} {}урона'.format(en.lower() + 'у', dmg, crit))
                if en_hp > 0:
                    hp -= en_dmg
                    en_hp -= reflect_value
                    print (' {} {}нанес тебе {} урона{}.\n ----------------------- \n'.format(en, evade, en_dmg, reflect))
                else:
                    print ('       и он умер\n ----------------------- \n')


            elif action == '2': #Если пропускаем, то просто получаем урон
                en_dmg = randint(en_min_dmg, en_max_dmg)
                #Способность воина на 50% отражение
                if hero_class == '1':
                    reflect_value = int(en_dmg/2)
                    reflect = ' и получил в ответ {} урона'.format(reflect_value)
                #Способность мага на 50% уклонение
                if hero_class == '3':
                    chance_evade = randint(1, 100)
                    if chance_evade >= 50:
                        en_dmg = 0
                        evade = 'промахнулся и '
                    else:
                        evade = ''
                hp -= en_dmg
                en_hp -= reflect_value
                print ('\n ----------------------- \n {} {}нанес тебе {} урона{}.\n ----------------------- \n'.format(en, evade, en_dmg, reflect))
            elif action == '3':
                if potion_count > 0:
                    heal = randint(1,10)
                    hp += heal
                    potion_count -= 1
                    print ('\n ----------------------- \n Ты выпил зелье и восстановил {} здоровья.\n ----------------------- \n'.format(heal))
                else:
                    print ('\n ----------------------- \n У тебя нет зелий здоровья.\n ----------------------- \n')
            else:
                print ('Ну написано же из чего выбирать. Не понял? Тогда пропускай ход.')
                en_dmg = randint(en_min_dmg, en_max_dmg)
                #Способность воина на 50% отражение
                if hero_class == '1':
                    reflect_value = int(en_dmg/2)
                    reflect = ' и получил в ответ {} урона'.format(reflect_value)
                #Способность мага на 50% уклонение
                if hero_class == '3':
                    chance_evade = randint(1, 100)
                    if chance_evade >= 50:
                        en_dmg = 0
                        evade = 'промахнулся и '
                    else:
                        evade = ''
                hp -= en_dmg
                en_hp -= reflect_value
                print ('\n ----------------------- \n {} {}нанес тебе {} урона{}.\n ----------------------- \n'.format(en, evade, en_dmg, reflect))
            if hp <=0:
                fight = False
            elif en_hp <=0:
                fight = False
        if hp <=0:
            print ('Упс, кажется, ты умер. Покойся с миром, {}.\n'.format(name))
            input ('За время путешествия ты убил {} и получил {} опыта.\n'.format(kill_count, exp_count))
            go = False #Если кончились хп персонажа
        elif en_hp <=0:
            print ('Вау, ты победил {}! Поздравляю, {}, ты получаешь {} опыта.\n'.format(en.lower() + 'а', name, add_exp))
            exp_count += add_exp
            potion_count += 1
            print ('Обыскав {}, ты нашел зелье здоровья! Теперь у тебя их {} шт.\n'.format(en.lower() + 'a', potion_count))
            still_go = input('Идем дальше?\n[1] - Да\n[2] - Нет, не хочу\n')
            kill_count += 1
            if still_go == '1' or still_go == '':
                go = True
            else:
                print ('\nНу что ж, не хочешь, как хочешь')
                go = False
                input ('За время путешествия ты убил {} и получил {} опыта.\n'.format(kill_count, exp_count))
#Надо вставить какую нибудь функцию,
#чтобы после смерти персонажа, можно было создать нового,
#а при отказе путешествовать - поменять класс
#я так делал в друком проекте, но он на другом компе и мне в падлу посмотреть


elif choise == '2':
    input ('\nА что не так? Хочешь поменять класс? Так вот, не в этой игре. Пока.')
else:
    input ('\nОпять ты ошибся. А впрочем ничего нового, запускай заново.')
    #pyinstaller.exe --onefile --icon=game.ico game.py - хуйня под создание экзешника
