import sys
import os
from math import sqrt

print('The commannd line arguments are: ')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH', sys.path, '\n')

print(os.getcwd())

print("Square root of 16 is", sqrt(16))