#!/usr/bin/env python
# coding=utf-8

import random
import sys

def guess_num(actual_num):
    step = 1
    while True:
        guess_num = raw_input('[+] enter number: ')
        if not guess_num.isdigit():
            print('invalid input, please input a number.')
            continue
        num = int(guess_num)
        if num == actual_num:
            print('you pass the game by ' + str(step) + ' steps, oh my baby, come on!')
            break
        elif num > actual_num:
            print('much bigger, try again.')
        else:
            print('too smaller, try again')
        step += 1

if __name__ == '__main__':
    print('[+]-----------------------------[+]')
    print('          Guess Number Game        ')
    print('[+]-----------------------------[+]')
    actual_num = random.randint(0, int(sys.argv[1]))
    guess_num(actual_num)
