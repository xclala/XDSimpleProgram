from math import pow
from time import strftime
from os import system

def func_1024():
    system("color f0")
    """Python中1024的显示"""

    result = [
        int(pow(2, 10)),
        2 ** 10,
        '1024',
        bin(1024),
        oct(1024),
        1024,
        hex(1024),
        strftime('%m%d'),
        '\n'.join([''.join([('1024'[(x - y) % 4] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in
            range(15, -15, -1)])

    ]

    for res in result:
        print(res)
    system("pause")


if __name__ == '__main__':
    func_1024()
