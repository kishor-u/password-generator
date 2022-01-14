#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project     : password_generator.py
@date        : 2022-01-15
@author      : kishor unnirkishnan
@description : api that generates secure passwords. as input parameters the user must provide
               the minimum length, the number of special characters, the number of numbers and
               the number of passwords that shall be created. Then generate the passwords 
               and return them in an array. Ex Input : 20 4 5 10
"""

# Importing required libraries.
import secrets
import string
import random


def generate_password(min_length, num_of_special_chars, num_of_digits):
    special_chars = ''.join(secrets.choice(list(string.punctuation))
                            for i in range(num_of_special_chars))
    digits = ''.join(secrets.choice(list(string.digits))
                     for i in range(num_of_digits))
    alphabets = ''.join(secrets.choice(list(string.ascii_letters)) for i in range(
        min_length - (num_of_special_chars + num_of_digits)))

    password = list(special_chars + digits + alphabets)
    random.shuffle(password)
    final_password = ''.join(password)
    return final_password


def main():

    stored_passwords = []
    min_length, num_of_special_chars, num_of_digits, num_of_pass = map(
        int, input().split())

    for _ in range(0, min_length):
        stored_passwords.append(generate_password(min_length, num_of_special_chars,
                                num_of_digits))

    print(stored_passwords)


if __name__ == '__main__':
    main()
