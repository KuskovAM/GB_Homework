import os
import sys
import shutil
import click
print('sys.argv = ', sys.argv)
print(os.getcwd()+os.path.basename(sys.argv[0]))

def print_help():
    print("help - получение справки")
    print("mkdir - создание директорий dir_1 - dir_9")
    print("deldir - удаляет директории dir_1 - dir_9")
    print("dirlist - список директрии рабочей папки")
    print("copyfile - сделать копию файла, из которого запускается скрипт")

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

def dir_list():
    dList = []
    dir_path = os.getcwd()
    for i in os.listdir(dir_path):
        if os.path.isdir(i) == True:
            dList.append(i)

    print('папки: ', dList)
def copy_file():
    try:
        dir_path = os.path.join(os.getcwd(), os.path.basename(sys.argv[0]))
        new_file_path = os.path.join(os.getcwd(), 'copy_file.py')
        print(dir_path)
        shutil.copyfile(str(dir_path), str(new_file_path))
    except FileExistsError:
        print('какая-то копия уже существует')

#------------------------ДЛЯ NORMAL-------------------------------------------
def print_help2normal():
    print("help2 - получение справки для normal")
    print("mkdir2 <dir_name> - создание директорию")
    print("deldir2 <dir_name>- удаляет директорию")
    print("dirlist2 - список директрии рабочей папки")
    print("gotodir <dir_name> - сделать копию файла, из которого запускается скрипт")
def make_dir2():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
def dir_list2():
    dList = []
    dir_path = os.getcwd()
    for i in os.listdir(dir_path):
        dList.append(i)
    print('папки: ', dList)

def del_dir2():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('директория {} отсутствует'.format(dir_name))

def go_to_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('переход в директорию {} успешен'.format(dir_name))
    except FileNotFoundError:
        print('переход в директорию {} провален, такой директории нет'.format(dir_name))

#-----------------------------------------------------------------------------
do = {
    "help": print_help,
    "mkdir": make_dir,
    "deldir": del_dir,
    "dirlist": dir_list,
    "copyfile": copy_file,
    "help2": print_help2normal,
    "mkdir2": make_dir2,
    "deldir2": del_dir2,
    "dirlist2": dir_list2,
    "gotodir": go_to_dir
}

# make_dir()
# del_dir()
#dir_list()
#copy_file()

# #---------для Normal-------------
#     try:
#         dir_name = sys.argv[2]
#     except IndexError:
#         dir_name = None
#     try:
#         key = sys.argv[1]
#     except IndexError:
#         key = None
#     if key:
#         if do.get(key):
#             do[key]()
#         else:
#             print("Задан неверный ключ")
#             print("Укажите ключ help для получения справки")


#---------для Easy-------------
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help или help2 для получения справки")
