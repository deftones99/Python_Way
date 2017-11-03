# Python中的format方法便是将每个参数值替换至格式所在的位置。

age = 20
name = 'Rose'
print("when {0} was {1} he wrote this book".format(name, age))

print("why {0} playing with that python".format(name))

# 数字是可选项，下面的方法同样可以

print("{} is {} years old".format(name, age))

# 对于浮点数'0.333'保留小数点后三位
print('{0:.3f}'.format(1 / 3))

# 使用下划线____填充字符串,并使总位数保持在11位
print('{0:_^11}'.format("hello"))

# 基于关键字进行输出
print('{name1} wrote this book when he was {age1}'.format(name1="ted", age1="24"))

# 对print()函数会自动换行的处理
print('a', end='')
print('b', end='')
print()
# 也可以指定以什么结尾
print('a', end=" ")
print('b', end=" this is truely end")
print()

# 转义，通过\反斜杠
print('what\'s that?')
# 也可以使用双引号
print("what's your plan?")
# 通过\n表示下一行
print('This is the first line\nThis is the second line')
# 在一行末尾添加的反斜杠表示字符串将在下一行继续，但不会添加新的一行
print("This is the first Sentence. \ "
      "This is the sencond Sentence")

# 对原始字符串的处理，这里处理了\n,在需处理的字符串前加r或者R
print(r'Newlines are indicate by \n')
print(R'Another Line is indicate by \n')


#关于缩进，不严谨的缩进可能引起错误,如在下列代码块中使用空格，将引起一个错误unexpected indent
i = 5
print('The Value is i')
print("fs")