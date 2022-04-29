import math
from datetime import datetime

go = 'yes'

# 'at' used to append to the end of a file and creates a new file if needed
with open('volumes.txt', 'at') as volumes:
    while go.lower() != 'no':
        date = datetime.now()
        w = int(input('Enter the width of the tire in mm (ex 205): ')) 
        a = int(input('Enter the aspect ratio of the tire (ex 60): ')) 
        d = int(input('Enter the diameter of the wheel in inches (ex 15): ')) 
        volume = (math.pi*w**2*a*(w*a + 2540*d)) / 10000000000
        print(f'\nThe approximate volume is {volume:.2f} liters')
        buy = input('Do you wish to buy tires with the dimensions you entered? ')

        if buy.lower() == 'yes':
            number = input('Please enter your phone number: ')
            print(f'{date:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}, {number}', file= volumes)
        else:
            print(f'{date:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}', file= volumes)

        go = input('\nDo you wish to add another set of dimensions?(yes/no) ')

    