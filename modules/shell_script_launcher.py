#!/usr/bin/env python3
from subprocess import run
from os import path


def run_shell_script(script_path):
    path_relative_to_script = f'{path.dirname(__file__)}/{script_path}'
    run(['/bin/sh', '-c', path_relative_to_script])


if __name__ == '__main__':
    print('This is a module, no routine without context!')
