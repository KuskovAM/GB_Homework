import os
import sys
print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir - создание директорий dir_1 - dir_9")
    print("deldir - удаляет директории dir_1 - dir_9")

def make_dir():
    i = 1
    while i < 10:
        k = str(i)
        dir_name = 'dir_'+ k
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
            print('директория {} создана'.format(dir_name))
        except FileExistsError:
            print('директория {} уже существует'.format(dir_name))
        i += 1

def del_dir():
    i = 1
    while i < 10:
        k = str(i)
        dir_name = 'dir_'+ k
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_path)
            print('директория {} удалена'.format(dir_name))
        except FileNotFoundError:
            print('директория {} отсутствует'.format(dir_name))
        i += 1

do = {
    "help": print_help,
    "mkdir": make_dir,
    "deldir": del_dir
}

#make_dir()
# del_dir()
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
