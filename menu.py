import random
from random import randint

dinnerNames = input('введіть список страв до вечері: ')

dinnerList = dinnerNames.split(', ')

total = 0
for dish in dinnerList:
    price = random.randint(100, 200)
    total = total + price
    print(dish + '.......' + str(price) + 'грн')
print('всього' + '.......' + str(total) + 'грн')
