def keyword(a, b=10, c=15):
    print("a is", a, "b is", b, "c is", c)


# a is 10 b is 14 c is 15
keyword(10, b=14)

# a is 100 b is 15 c is 50 参数还可打乱顺序
keyword(c=50, b=15, a=100)

# a is 22 b is 10 c is 31
keyword(a=22, c=31)

# a is 3 b is 7 c is 15
keyword(3, 7)
