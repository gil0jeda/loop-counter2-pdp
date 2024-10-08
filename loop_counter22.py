"""
Author: Gilberto Ojeda
Date: 2024-10-6
Description: ask user for 2 numbers that are more than 0
# the second has to be larger than the first, afte print numbers that are
in between these two and sum them
"""



def main():

    print('Welcome to our counting program.')
    print('( it also adds up the digits counted! )')

    try:
        number1, number2 = inputs()

        counted_numbers, total_sum = processing(number1, number2)

        output(counted_numbers, total_sum)

        restart = input('Continue? Enter y or no')
        if restart == 'y' or restart == 'Y':
            print('Ok, lets do this again')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
            print(err)


def inputs():

    number1 = get_pos_num('Please enter a small number:')
    number2 = get_pos_num(f'Please enter a whole number larger than {number1}:')

    while number2 <= number1:
        print(f'The second number must be larger than {number1}.')
        number2 = get_pos_num(f'Please enter a number larger than {number1}: ')

    return number1, number2


def processing(number1, number2):

    counted_numbers = []
    total_sum = 0

    for num in range(int(number1), int(number2) + 1):
        print(num)
        counted_numbers.append(num)
        total_sum += num
    return counted_numbers, total_sum

def output(counted_numbers, total_sum):

    print(f'The numbers counted are: {counted_numbers}')
    print(f'The total  of counted number is: {total_sum}')



def get_pos_num(prompt):
            """
            Gets a positive number from a user. Prompts the user for a number, validates that it's a positive number, and
            will not return until a valid entry is received.

            :return: A positive number
            """
            while True:
                try:
                    pos_int = float(input(f'{prompt} (positive numbers only) '))
                    if pos_int >= 0:
                        break
                    else:
                        print("The number must be greater than zero.")
                except ValueError:
                    print("Only digits and a decimal point are allowed.")
            return pos_int

main()