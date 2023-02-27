import commands

def check_int(x):
    try:
        x = int(x)
        return True
    except ValueError:
        print('Ошибка ввода!')
        return False

def quit_input(check_input):
    exit_prove = (check_input == '<')
    if exit_prove:
        while True:
            still_prove = input('Вы уверены? (">" - да, "<" - нет): ')
            if still_prove == '>':
                return True
            elif still_prove == '<':
                return False
            else:
                print('Ошибка ввода!')

def skip_cancel(text):
    if text == '>' or text == '-r':
        return 'skip'
    elif text == '<' or text == '-d':
        return 'cancel'
    else:
        return 'pass'

def check_input(text, range_val):
    if skip_cancel(text) == 'cancel':
        return 2
    else:
        if not check_int(text):
            return 0
        else:
            if not int(text) - 1 in range(0, range_val):
                print('Ошибка ввода!')
                return 0
            return 1