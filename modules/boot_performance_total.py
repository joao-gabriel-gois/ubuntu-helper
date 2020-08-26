#!/usr/bin/env python3
import re
from subprocess import run
import os


def create_raw_blame_file_and_analyze(analyze):
    run('sudo systemd-analyze blame > /tmp/.blame.txt')

    file = open('/tmp/.blame.txt', 'r')

    if callable(analyze):
        analyze(file)
    else:
        print('Only acceptable argument is a function!')

    file.close()

    os.remove('/tmp/.blame.txt')


def print_perfomance_total(file):
    line_time_digit_clean_list = []
    total = 0

    for line in file:
        raw_one_item_in_string_number_list = re.findall(
            "\d+\.\d+|\d+[m]", str(line)
        )
        
        for number_in_string in raw_one_item_in_string_number_list:
            dot_char_index = number_in_string.find('.')
            m_char_index = number_in_string.find('m')

            if dot_char_index != -1:
                clean_number = number_in_string.replace('.', '')
            if m_char_index != -1:
                clean_number = number_in_string.replace('m', '')

            line_time_digit_clean_list.append(int(clean_number))

    for task_time_took_in_ms in line_time_digit_clean_list:
        total = total + task_time_took_in_ms

    total_in_min = round((total / 60000), 3)
    total_in_sec = total_in_min * 60

    total_in_min_string = str(total_in_min) + ' minutes'
    total_in_sec_string = str(total_in_sec) + ' seconds'

    time = total_in_min_string if total_in_min > 1 else total_in_sec_string

    print(f'This time your system took {time} to boot')


def main():
    create_raw_blame_file_and_analyze(print_perfomance_total)


if __name__ == '__main__':
    main()
