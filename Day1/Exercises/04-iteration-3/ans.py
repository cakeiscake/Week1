# * Create a variable and assign it to the array below
from statistics import median, mode

arr = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]


# * Write a function that will take in this variable
# * It will return the median number in the array
# * It will return the average of that array
# * It will return the number that occurs most frequently in the array

def myfunc(arr):
   total = sum(arr)
   med = median(arr)
   mod = mode(arr)
   avg =  total // len(arr)
   return med,mod,avg

print(myfunc(arr))
