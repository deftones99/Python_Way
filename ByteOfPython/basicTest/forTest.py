for i in range(1, 5):
    print(i)
else:
    print("Loop is over!")

    # 在默认情况下，range将会以1逐步的递增，如果向range函数中再增加一个数字，如range(1,10,2)则这个数字会成为
    # 逐步递增的加数

for i in range(1, 10, 2):
    print(i)
else:
    print("Loop is over!")
