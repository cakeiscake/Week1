# # * Write a for loop that will take in a number.
# * When the loop is called it will iterate from `0` forward towards that number and print all the values in between to the terminal.
# * Write another loop that will do the same thing but iterate backwards from that number to zero.

def my_loop(x):
    for i in range(x):
        print(i)
        

def my_reverse_loop(y):
    for i in reversed(range(y)):
        print(i)


my_loop(10)
print()
my_reverse_loop(10)