import pickle

# 储存对象的文件名
shop_list_file = 'shopList.data'

shop_list = ['apple', 'mango', 'carrot']

f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()


del shop_list
# if shop_list:
#     print(shop_list)
# else:
#     print('没有定义 shop_list')

f = open(shop_list_file, 'rb')
shop_list = pickle.load(f)
print(shop_list)