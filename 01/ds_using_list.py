# This is my shopping list
shopList = ['apple', 'mango', 'carrot', 'bannana']
print("I have", len(shopList), 'items to purchase.')

print('These items are', end = '')
for item in shopList:
    print(item, end=", ")

print('\nalso have buy rice.')
shopList.append('rice')
print('my shopList is now', shopList)

print('I will sort my list now')
shopList.sort()
print('my shopList is now', shopList)

print('the first item i will buy is', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('i bought the', oldItem)
print('my shopping list now', shopList)