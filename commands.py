import check_input
import globals as g
import json
import check_input as check

g.input_str = ''

phone_type = ['моб.', 'раб.']
mail_type = ['личн.', 'раб.']
find_list = ['Фамилия', 'Имя', 'Отчество', 'Телефоны', 'Почта']
new_dict = {
    'Фамилия:': '',
    'Имя:': '',
    'Отчество:': '',
    'Телефоны:': {},
    'Почта:': {},
}


def help_output(help_dict):
    for k, v in help_dict.items():
        print('{0:8s}:{1}'.format(k, v))

def quit_mess():
    print('Бот завершил свою работу!')
    print('Изменения сохранены!')
    print('До новых встреч в эфире!')
    with open('phones.json', 'w') as f:
        json.dump(g.data, f, indent=2)
    exit()

def add():
    input_dict = {
        'Фамилия:': 'Введите фамилию ',
        'Имя:': 'Введите имя: ',
        'Отчество:': 'Введите отчество: ',
        'Телефоны:': 'Введите телефон: ',
        'Почта:': 'Введите почту: ',
    }

    for k,v in input_dict.items():
        flag = False
        skip = False

        if not k == 'Телефоны:' and not k == 'Почта:':
            while True:
                text_input = input(input_dict[k] + '(< - отмена ввода, > - пропустить): ')
                if check_input.skip_cancel(text_input) == 'skip':
                    skip = True
                    break
                elif check_input.skip_cancel(text_input) == 'cancel':
                    if check.quit_input(text_input):
                        flag = True
                        break
                else:
                    break
            if skip:
                continue
            if flag:
                break
            new_dict[k] = text_input

        else:
            while True:
                flag = False
                skip = False
                if k =='Телефоны:':
                    key_type = phone_type[:]
                else:
                    key_type = mail_type[:]
                print(input_dict[k])
                idx_own = 1
                idx_work = 1

                while True:
                    for k_ph, v_ph in enumerate(key_type):
                        print(f'[{k_ph + 1}] - {v_ph} ')
                    text_input = input('Выбирите тип (< - отмена, > - пропустить): ')
                    if check_input.skip_cancel(text_input) == 'cancel':
                        if check.quit_input(text_input):
                            flag = True
                            break
                        else:
                            continue
                    if check_input.skip_cancel(text_input) == 'skip':
                        skip = True
                        break
                    if not check.check_int(text_input):
                        continue
                    else:
                        if int(text_input) not in range(0, 3):
                            print('Ошибка ввода!')
                            continue
                        break

                if skip:
                    break
                if flag:
                    break

                if int(text_input) - 1 == 0:
                    key_idx_add = idx_own
                    idx_own += 1
                else:
                    key_idx_add = idx_work
                    idx_work += 1

                key_input = int(text_input)

                while True:
                    text_input = input(input_dict[k] + '(< - отмена): ')
                    if check_input.skip_cancel(text_input) == 'cancel':
                        if check.quit_input(text_input):
                            flag = True
                            break
                        else:
                            continue
                    else:
                        new_dict[k][key_type[key_input - 1] + str(key_idx_add)] = text_input
                        break
                if flag:
                    break

                while True:
                    text_input = input('Еще разок? (> - да, < -  нет) \n> ')
                    if check.skip_cancel(text_input) == 'cancel':
                        skip = True
                        flag = True
                        break
                    elif check.skip_cancel(text_input) == 'skip':
                        break
                    else:
                        print('Ошибка ввода!')

                if flag:
                    break
            if skip:
                continue
            if flag:
                break
        if flag:
            break
    else:
        g.data.append(new_dict)
        index = len(g.data) - 1
        find_contact('none', index, search='index')
        print('\nКонтакт успешно добавлен в список контактов!\n')

def find_contact(key_search, string_search, search):
    if search == 'all' and string_search == 'all':
        for items in g.data:
            for key, val in items.items():
                print(f'{key:<12}{val if type(val) == str else ", ".join("{}: {}".format(k, v) for k, v in val.items())}')
            print('-' * 40)

    if search == 'index':
        for key, val in g.data[string_search].items():
            print(f'{key:<12}{val if type(val) == str else ", ".join("{}: {}".format(k, v) for k, v in val.items())}')

    if search == 'string':
        print_sep = False
        if type(string_search) == str:
            for i in range(len(g.data)):
                found = False
                for k,v in g.data[i].items():
                    if type(v) == str:
                        if k == key_search and v.find(string_search) != -1:
                            found = True
                            print_sep = True
                            print('-' * 40)
                            for key,val in g.data[i].items():
                                print(f'{key:<12}{val if type(val) == str else ", ".join("{}: {}".format(k, v) for k, v in val.items())}')
                    if type(v) == dict:
                        for key, val in v.items():
                            if k == key_search and val.find(string_search) != -1 and not found:
                                found = True
                                print_sep = True
                                print('-' * 40)
                                for a,b in g.data[i].items():
                                    print(f'{a:<12}{b if type(b) == str else ", ".join("{}: {}".format(k, v) for k, v in b.items())}')
                if print_sep:
                    print('-' * 40)
                    print_sep = False
            if not found:
                print('Ничего не найдено!')


def find():
    print('Поиск по...')
    while True:
        flag = False
        while True:
            for k, v in enumerate(find_list):
                print(f'[{k + 1}] - {v}')
            text_input = input('Выбирите тип (< - отмена): ')
            range_val = len(find_list)
            if check.check_input(text_input, range_val) == 0:
                continue
            elif check.check_input(text_input, range_val) == 1:
                break
            else:
                flag = True
                break
        if flag:
            break

        search_key = find_list[int(text_input) - 1] + ':'
        search_str = input(find_list[int(text_input) - 1] + ' (< - отмена): ')
        if search_str == '<':
            break

        find_contact(search_key, search_str, 'string')
        break

def delete():
    text_input = ''
    while True:
        temp_list = []
        flag = False
        for item in g.data:
            fio = ''
            for k, v in item.items():
                if k == 'Фамилия:' or k == 'Отчество:' or k == 'Имя:':
                    fio += v + ' '
            temp_list.append(fio)

        for k, v in enumerate(temp_list):
            print(f'[{k + 1}] - {v}')

        while True:
            text_input = input('Введите номер контакта из списка (< - отмена): ')
            range_val = len(temp_list)
            if check.check_input(text_input, range_val) == 0:
                continue
            elif check.check_input(text_input, range_val) == 1:
                break
            else:
                flag = True
                break

        if flag:
            break

        while True:
            cmd_input = input('Введите комманду (-d - удалить, -r - редактировать): ')
            if check_input.skip_cancel(cmd_input) == 'skip':
                break
            elif check_input.skip_cancel(cmd_input) == 'cancel':
                break
            else:
                print('Ошибка ввода!')

        if flag:
            break

        contact_key = int(text_input) - 1
        if cmd_input == '-d':
            while True:
                text_input = input(f'Удалить {temp_list[int(contact_key)]} (< - отмена, > - удаление): ')
                if check.skip_cancel(text_input) == 'cancel':
                    flag = True
                    break
                elif check.skip_cancel(text_input) == 'skip':
                    print()
                    del g.data[contact_key]
                    print('Контакт удален!')
                    flag = True
                    print(g.data)
                    break
                else:
                    print('Ошибка ввода!')

            if flag:
                break

        if cmd_input == '-r':
            key_list = []
            for key, val in new_dict.items():
                key_list.append(key)

            for k, v in enumerate(key_list):
                print(f'[{k + 1}] - {v}')

            while True:
                text_input = input('Что редактируем? (< - отмена): ')
                range_val = len(key_list)
                if check.check_input(text_input, range_val) == 0:
                    continue
                elif check.check_input(text_input, range_val) == 1:
                    break
                else:
                    flag = True
                    break
            if flag:
                break

            edit_key = key_list[int(text_input) - 1]
            if type(g.data[contact_key].get(edit_key)) == str:
                text_input = input('Введите новые данные (< - отмена): ')
                if check.skip_cancel(text_input) == 'cancel':
                    flag = True
                    break
                g.data[contact_key][edit_key] = text_input
                print('Изменения внесены успешно!')
                find_contact('none',contact_key, search = 'index')
                break

            if type(g.data[contact_key].get(edit_key)) == dict:
                key_list = []
                idx = 1
                for key, val in g.data[contact_key].get(edit_key).items():
                    key_list.append(key)
                    print(f'[{idx}] - {key}: {val}')
                    idx += 1

                while True:
                    text_input = input('Что редактируем? (< - отмена): ')
                    range_val = len(key_list)
                    if check.check_input(text_input, range_val) == 0:
                        continue
                    elif check.check_input(text_input, range_val) == 1:
                        break
                    else:
                        flag = True
                        break
                if flag:
                    break

                sub_edit_key = key_list[int(text_input) - 1]
                text_input = input('Введите новые данные (< - отмена): ')
                if check.skip_cancel(text_input) == 'cancel':
                    flag = True
                    break
                g.data[contact_key][edit_key][sub_edit_key] = text_input
                print('Изменения внесены успешно!')
                find_contact('none', contact_key, search='index')
                break
            if flag:
                break

