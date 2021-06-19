import ctypes

from classes import FsState
from output import print_result


def execute_command(operation, libmy_ext, fs_state):
    if operation.command == 'ls':
        libmy_ext.execute_ext_ls.restype = ctypes.c_char_p
        libmy_ext.execute_ext_ls.argtypes = [ctypes.POINTER(FsState)]
        result = libmy_ext.execute_ext_ls(fs_state)
        print_result(result)

    elif operation.command == 'pwd':
        libmy_ext.execute_ext_pwd.restype = ctypes.c_char_p
        libmy_ext.execute_ext_pwd.argtypes = [ctypes.POINTER(FsState)]
        result = libmy_ext.execute_ext_pwd(fs_state)
        print_result(result)

    elif operation.command == 'cd':
        libmy_ext.execute_ext_cd.restype = ctypes.c_char_p
        libmy_ext.execute_ext_cd.argtypes = [ctypes.POINTER(FsState), ctypes.c_char_p]
        result = libmy_ext.execute_ext_cd(fs_state, operation.first_argument.encode('UTF-8'))
        if result is not None:
            print_result(result)

    elif operation.command == 'cp':
        libmy_ext.execute_ext_cp.restype = ctypes.c_void_p
        libmy_ext.execute_ext_cp.argtypes = [ctypes.POINTER(FsState), ctypes.c_char_p, ctypes.c_char_p]
        libmy_ext.execute_ext_cp(fs_state,
                                 operation.first_argument.encode('UTF-8'), operation.second_argument.encode('UTF-8'))
    else:
        libmy_ext.execute_help.restype = ctypes.c_char_p
        result = libmy_ext.execute_help()
        print_result(result)
