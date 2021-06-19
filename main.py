import pathlib
import sys
import ctypes

import classes
from output import print_partitions
from user_interface import dialog


def main():
    libname = pathlib.Path().absolute() / "libmy_ext.so"
    libmy_ext = ctypes.CDLL(libname)
    libmy_ext.get_partitions.restype = ctypes.POINTER(classes.Output)
    args = sys.argv[1:]
    mode = None
    path = None
    if len(args) > 4:
        print("Неверный режим работы")
    else:
        for i in range(0, len(args), 2):
            if args[i] == '-m':
                mode = args[i + 1]
            elif args[i] == '-p':
                path = args[i + 1]
    if mode == '1':
        result = libmy_ext.get_partitions()
        print_partitions(result)
    elif mode == '2' and path != '':
        dialog(path, libmy_ext)
    else:
        print("Неверный режим работы")


main()
