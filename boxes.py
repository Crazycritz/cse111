import math

num_items = int(input('Enter the number of iems: '))
num_box = int(input('Enter the number of items per box: '))

boxes = math.ceil(num_items/num_box)
print(f'For {num_items} items, packing {num_box} items in each box, you will need {boxes} boxes.')
