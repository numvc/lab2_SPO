from array import array


def print_partitions(result):
    print("/dev/{:}\t\tdisk\t\t\t{:.3f} GB".format(result.contents.d_name.decode(), result.contents.size))
    print(result.contents.information.decode())


def print_result(result):
    print(result.decode())
