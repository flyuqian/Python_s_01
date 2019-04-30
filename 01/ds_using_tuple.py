# () 是可选项, 用来指明开始和结束, 推荐一直使用

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Nunber of cages in the new_zoo is', len(new_zoo))

print('animals brought from old zoo are', new_zoo[2])
print('last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo) + len(new_zoo[2]) - 1)
