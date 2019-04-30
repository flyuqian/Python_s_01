

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
my_list = shoplist

del shoplist[0]

print('shop_list', shoplist)
print('my list', my_list)


my_list = shoplist[:]
del shoplist[0]
print('shop_list', shoplist)
print('my list', my_list)