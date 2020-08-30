#!/usr/bin/env python3
class colors:
    NC = '\033[90m'
    RE = '\033[91m'
    GR = '\033[92m'
    YE = '\033[93m'
    PU = '\033[94m'
    PI = '\033[95m'
    BL = '\033[96m'
    END = '\033[m'
    BLD = '\033[1m'
    UNDLN = '\033[4m'


if __name__ == "__main__":
    print('\nCheck all possibilites that this color class has:\n')
    c = colors()
    for i in range(0, 7):
        print(f'\033[9{i}mtest{c.END}')
    print(f'\n{c.BL}{c.BLD}test{c.END}')
    print(f'{c.PI}{c.UNDLN}test{c.END}')
