#!/usr/bin/env python3
from subprocess import Popen


def run_shell():
    Popen(['/bin/sh', '-c', 'shell-script/updater'])


if __name__ == '__main__':
    run_shell()
