#!/usr/bin/env python
# coding=utf-8

import random
import sys

def guess_num(actual_num):
    step = 1
    while True:
        guess_num = input('[+] enter number: ')
        if not isinstance(guess_num, int):
            print('please input a number.')
            continue
        if guess_num == actual_num:
            print('you pass the game by ' + str(step) + ' steps, oh my baby, come on!')
            break
        elif guess_num > actual_num:
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
