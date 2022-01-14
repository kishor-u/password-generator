#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project     : password-generator.py
@date        : 2022-01-15
@author      : kishor unnirkishnan
@description : api that generates secure passwords. as input parameters the user must provide
               the minimum length, the number of special characters, the number of numbers and
               the number of passwords that shall be created. Then generate the passwords 
               and return them in an array.

               Sample GET Request: http://localhost:8080/password-generator?min_length=20&
                            num_of_special_chars=4&num_of_digits=6&num_of_pass=10

"""

# Importing required libraries.
from flask import Flask, request
import secrets
import string
import random

app = Flask(__name__)


def generate_secure_password(min_length, num_of_special_chars, num_of_digits):
    special_chars = ''.join(secrets.choice(list(string.punctuation))
                            for i in range(num_of_special_chars))
    digits = ''.join(secrets.choice(list(string.digits))
                     for i in range(num_of_digits))

    alphabet_count = min_length - (num_of_special_chars + num_of_digits)

    alphabets = ''.join(secrets.choice(list(string.ascii_letters))
                        for i in range(alphabet_count))

    password = list(special_chars + digits + alphabets)
    random.shuffle(password)
    final_password = ''.join(password)
    return final_password


@app.route('/password-generator', methods=['GET'])
def password_generator():

    generated_passwords = []

    args = request.args
    min_length = int(args.get('min_length'))
    num_of_special_chars = int(args.get('num_of_special_chars'))
    num_of_digits = int(args.get('num_of_digits'))
    num_of_pass = int(args.get('num_of_pass'))

    # Basic validation checks
    if(min_length - (num_of_special_chars + num_of_digits) < 0):
        return {"message": "Arguments mismatch. Please check!"}
    elif(any(x < 0 for x in [min_length, num_of_special_chars, num_of_digits, num_of_pass])):
        return {"message": "Negetive arguments provided. Please check!"}
    else:
        for _ in range(num_of_pass):
            generated_passwords.append(generate_secure_password(min_length, num_of_special_chars,
                                                                num_of_digits))
        return {"password_array": generated_passwords}


# Run the flask application
app.run(host="0.0.0.0", port="8080", debug=True)
