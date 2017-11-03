# set是无序的
bri = set(['usa', 'russia', 'india'])

print(len(bri))  # 3
print(bri)  # {'russia', 'usa', 'india'}

print('india' in bri)  # True
print('china' in bri)  # False

bric = bri.copy()
bric.add('china')
print(bric)  # {'india', 'usa', 'russia', 'china'}
print(bric.issuperset(bri))  # True

bri.remove('russia')
print(bri)  # {'india','usa'}
print(bri&bric)  # {'usa', 'india'}
