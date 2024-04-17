# A function will take a number and return its square

def square_num(num):
    square = num**2
    return square


number = square_num(int(input('Enter a number: ')))
print(f'The square of your number is {number}')