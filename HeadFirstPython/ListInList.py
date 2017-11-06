from HeadFirstPython.printLoL import print_lol, print_lol2, print_lol3

movies = ['The Holy Shit', 1975, 'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman',
           ['Michael Palin', 'Jone Cleese', 'Terry Giliam', 'Eric Idle', 'Terry Jones']
           ]
          ]

print('输出Movies列表:')
print(movies)
print()
for each_movie in movies:
    if isinstance(each_movie, list):
        for each_movie1 in each_movie:
            if isinstance(each_movie1, list):
                for each_movie2 in each_movie1:
                    print(each_movie2)
            else:
                print(each_movie1)
    else:
        print(each_movie)

"""print(movies[4][1][0])"""

print('使用函数处理Movies列表:')

print_lol(movies)
print('使用新函数处理Movies列表:')
print_lol2(movies, 3)
print('使用print_lol3处理Movies列表：')
print('####1')
print_lol3(movies)
print('####2')
print_lol3(movies, True)
print('####3')
print_lol3(movies, True, 1)
