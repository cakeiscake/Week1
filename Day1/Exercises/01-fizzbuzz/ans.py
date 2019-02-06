
# * Write a function that will take a number as an argument.
# * The function will loop from 0 to the number.
# * If the number is divisible by 3 print `Fizz` to the terminal.
# * If the number is divisible by 5 print `Buzz` to the terminal.
# * if the number is divisible by 3 and 5 print `FizzBuzz` to the terminal.

def FizzBuzz(n):
    for i in range(n):
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        if i % 15 == 0:
            print('FizzBuzz')

FizzBuzz()