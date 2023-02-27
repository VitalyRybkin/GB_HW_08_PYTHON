import commands as cmds
import globals as g
import json
g.data = []
g.temp_dict = {}

help_dict = {
    'h': 'Справка',
    's': 'Начать работу',
    'Q': 'Завершить работу',
    'a': 'Добавить контакт',
    'd': 'Удалить/редактировать контакт',
    'w': 'Показать справочник',
    'f': 'Найти',
}

print('Добро пожаловать в телефонный справочник!')
while True:
    cmd = input('Введите комманду (> h - справка, > s - начало работы, > Q - завершить)\n> ')
    if not cmd == 'h' and not cmd == 's':
        print('Введена неверная команда!')
        continue
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 's':
        print('Бот начал свою работу!')
        with open('phones.json', 'r') as f:
            g.data = json.load(f)
        break
    if cmd == 'Q':
        cmds.quit_mess()


while True:
    cmd = input('Введите комманду (\'Q\' - завершить): \n> ')
    if cmd not in help_dict:
        print('Команды не существует!')
        cmds.help_output(help_dict)
        continue
    if cmd == 'Q':
        cmds.quit_mess()
    if cmd == 's':
        print('Бот уже трудится!')
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 'a':
        cmds.add()
    if cmd == 'w':
        cmds.find_contact('none','all', 'all')
    if cmd == 'f':
        cmds.find()
    if cmd == 'd':
        cmds.delete()
