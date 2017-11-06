movies = ["The Holy Shit", "The Life of Brain", "The Meaning of Life"]

print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

"""在列表后加如一个"""
cast.append("Gliliam")
print(cast)

"""删除尾部最后一个"""
cast.pop()
print(cast)

"""在列表中扩展一个新列表"""
cast.extend(["Gliliam", "Chapman"])
print(cast)

"""扩展电影列表"""
movies.insert(1, 1995)
movies.insert(3, 2001)
movies.append(2007)
print(movies)

print("\n使用for循环处理列表：")
"""使用for循环处理列表"""
for each_movie in movies:
    print(each_movie)

print("\n使用while循环处理列表：")
"""使用while循环处理列表"""
count = 0
while count < len(movies):
    print(movies[count])
    count += 1
