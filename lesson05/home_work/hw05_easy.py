# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print('*****TASK 1*****', '\n')


def new_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except Exception:
        print('Something got wrong with  ' + dir_name)


def new_dirs():
    for i in range(1,10):
        new_dir('dir_' + str(i))


print(os.listdir("."))


def delete_dir(dir):
    try:
        os.rmdir(dir)
    except Exception:
        print('Something wrong with remove ' + dir)


def delete_dirs():
    for i in range(1, 10):
        delete_dir('dir_' + str(i))


new_dirs()
print(os.listdir("."), '\n')
delete_dirs()

print('*****END OF TASK 1*****', '\n')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('*****TASK 2*****', '\n')


def show_dirs():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

new_dirs()
show_dirs()
delete_dirs()

print('\n', '*****END OF TASK 2*****', '\n')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('*****TASK 3*****', '\n')
print(os.listdir("."), '\n')


def copy_file(source, loc):
    with open(source, 'r', encoding="utf-8") as src, open(loc, 'w', encoding="utf-8") as dst: dst.write(src.read())


copy_file(os.path.basename(__file__), os.path.basename(__file__) + '.copy')

print(os.listdir("."), '\n')
print('\n', '*****END OF TASK 3*****', '\n')

