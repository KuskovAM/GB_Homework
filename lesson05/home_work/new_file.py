import os
import sys
import shutil
print('sys.argv = ', sys.argv)
print(os.getcwd()+os.path.basename(sys.argv[0]))

def print_help():
    print("help - получение справки")
    print("mkdir - создание директорий dir_1 - dir_9")
    print("deldir - удаляет директории dir_1 - dir_9")
    print("dirlist - список директрии рабочей папки")

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
    dir_path = os.path.join(os.getcwd(), os.path.basename(sys.argv[0]))
    new_file_path = os.path.join(os.getcwd(), 'new_file.py')
    print(dir_path)
    shutil.copyfile(str(dir_path), str(new_file_path))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "deldir": del_dir,
    "dirlist": dir_list,
    "copyfile": copy_file
}

# make_dir()
# del_dir()
#dir_list()
copy_file()
# try:
#     key = sys.argv[1]
# except IndexError:
#     key = None
# if key:
#     if do.get(key):
#         do[key]()
#     else:
#         print("Задан неверный ключ")
#         print("Укажите ключ help для получения справки")
