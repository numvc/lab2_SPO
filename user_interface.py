import ctypes

from classes import Operation, FsState
from execution import execute_command


def parse_command(command):
    lst = command.split(" ")
    operation = Operation
    for i in range(len(lst)):
        if i == 0:
            operation.command = lst[i]
        elif i == 1:
            operation.first_argument = lst[i]
        elif i == 2:
            operation.second_argument = lst[i]
    return operation


def dialog(path, libmy_ext):
    fs_state = FsState()
    libmy_ext.setup.restype = ctypes.POINTER(FsState)
    fs_state = libmy_ext.setup(ctypes.c_char_p(path.encode('UTF-8')))
    if fs_state:
        print("Введите команду")
        command = input()
        operation = parse_command(command)
        while operation.command != 'quit':
            execute_command(operation, libmy_ext, fs_state)
            print("Введите команду")
            command = input()
            operation = parse_command(command)
        print("Завершение работы")
