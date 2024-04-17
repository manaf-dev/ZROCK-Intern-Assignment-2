# Program uses try-except block to handle a division by zero error.

def handle_division(numerator, denominator):

    try:
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print('Error! You cannot divide by Zero.')

#Test 1
num_1 = 8
deno_1 = 2
handle_division(num_1, deno_1)

#Test 2
num_2 = 9
deno_2 = 0
handle_division(num_2, deno_2)