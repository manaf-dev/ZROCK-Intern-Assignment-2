# Program to use sqrt function from the math module

import math

def sqrt_num(num):
    result = math.floor(math.sqrt(num)) #remove the decimal point with floor function
    print(f'The square root of {num} is {result}')

sqrt_num(int(input('Enter a number: ')))