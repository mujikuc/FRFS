import sqlite3
import random
import sys

#Начало работы с БД
conn = sqlite3.connect("my.db")
c = conn.cursor()


# #Создание таблицы в БД
# c.execute("""CREATE TABLE classes
#                    (num, name, hp, skill)
#                    """)
# conn.commit()
#
# #Добавление данных в таблицу
# # add_enemy = [('1', 'Бандит', '10', '1', '4'),
# #            ('2', 'Орк', '15','1', '8'),
# #            ('3', 'Волк', '8','2', '6')]
# add_date = [('1', 'Воин', '20', 'Стальная кожа (-1 получаемого урона)'),
#            ('2', 'Убийца', '15','Меткий удар (25% двойного урона)'),
#            ('3', 'Маг', '10', 'Магический барьер (40% уклонения)'),
#            ('4', 'Непонятно что', '5', 'Нет')]
# c.executemany("INSERT INTO classes VALUES (?,?,?,?)", add_date)
# conn.commit()


def random_enemy():
    #Начало работы с БД
    conn = sqlite3.connect("my.db")
    c = conn.cursor()
    #Определение количества строк в БД для правильного расчета рандома
    c.execute("SELECT COUNT(*) FROM enemies")
    len = c.fetchone()[0]

    #рандомный выбор противника из БД
    en_key = str(random.randint(1, len))
    c.execute("SELECT * FROM enemies WHERE num=?", en_key)

    # Запись характеристик выбранного противника
    enemy_list = c.fetchone()
    en_name = enemy_list[1]
    en_hp = enemy_list[2]
    en_min_dmg = enemy_list[3]
    en_max_dmg = enemy_list[4]

    print ('''Противник: {}
    Здоровье: {}
    Минимальный урон: {}
    Максимальный урон: {}'''.format(en_name, en_hp, en_min_dmg, en_max_dmg))


#Вывод всех противников и их характеристик
def bestiary():
    #Начало работы с БД
    conn = sqlite3.connect("my.db")
    c = conn.cursor()
    #Определение количества строк в таблице для правильного расчета предела i
    c.execute("SELECT COUNT(*) FROM enemies")
    len = c.fetchone()[0] + 1

    print('Бестиарий: \n')
    for i in range(1, len):
        #хз почему, но передать i в запрос можно только так
        key = str(i)
        #Выбор противников и заполнение их характеристик
        c.execute("SELECT * FROM enemies WHERE num=?", key)
        enemy_list = c.fetchone()
        print ('''Противник №{}: {}
        Здоровье: {}
        Минимальный урон:  {}
        Максимальный урон: {}
       -------------------'''.format(i, enemy_list[1], enemy_list[2], enemy_list[3], enemy_list[4]))

def merch():
    #Начало работы с БД
    conn = sqlite3.connect("my.db")
    c = conn.cursor()
    #Определение количества строк в таблице для правильного расчета предела i
    c.execute("SELECT COUNT(*) FROM weapons")
    len = c.fetchone()[0] + 1

    print('Оружие: \n')
    for i in range(1, len):
        #хз почему, но передать i в запрос можно только так
        key = str(i)
        #Выбор оружия и заполнение его характеристик
        c.execute("SELECT * FROM weapons WHERE num=?", key)
        weapon_list = c.fetchone()
        print ('''Оружие №{}: {}
        Минимальный урон:  {}
        Максимальный урон: {}
       -------------------'''.format(i, weapon_list[1], weapon_list[2], weapon_list[3]))

def classes():
    #Начало работы с БД
    conn = sqlite3.connect("my.db")
    c = conn.cursor()
    #Определение количества строк в таблице для правильного расчета предела i
    c.execute("SELECT COUNT(*) FROM classes")
    len = c.fetchone()[0] + 1

    print('Классы: \n')
    for i in range(1, len):
        #хз почему, но передать i в запрос можно только так
        key = str(i)
        #Выбор класса и заполнение его характеристик
        c.execute("SELECT * FROM classes WHERE num=?", key)
        class_list = c.fetchone()
        print ('''Класс №{}: {}
        Здоровье:  {}
        Способность: {}
       -------------------'''.format(i, class_list[1], class_list[2], class_list[3]))
classes()
