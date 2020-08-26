#!/usr/bin/env python3
from modules.boot_performance_total import main
from modules.updater import run_update_shell


if __name__ == '__main__':
    command = ''
    while command not in ['0', '1', '2']:
        command = input(
          'To update press 1\
          \nTo check boot performance press 2\
          \nTo close press 0'
        )

    if command == '1':
        run_update_shell('modules/shell-script/updater')
    elif command == '2':
        main()
    elif command == '0':
        exit()

else:
    print('This is a script, not a module!')
