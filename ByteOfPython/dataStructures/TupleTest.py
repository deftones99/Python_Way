# 元祖的使用，元祖是不可变的，不像List一样具有众多属性
zoo = ('cat', 'dog', 'python')

print('Number of zoo is :', len(zoo))

new_zoo = ('elephant', 'lion', zoo)

print('Number of cages in the new zoo is:', len(new_zoo))
print('All animal in new zoo are:', new_zoo)
print('Animal bought from old zoo are:', new_zoo[2])
print('Last animal bought from old zoo is:', new_zoo[2][2])
print('Number of animal in new zoo are:', len(new_zoo) - 1 + len(new_zoo[len(new_zoo) - 1]))
