#!/usr/bin/env python3
from subprocess import run


def run_update_shell(path):
    run(['/bin/sh', '-c', path])


if __name__ == '__main__':
    run_update_shell()
