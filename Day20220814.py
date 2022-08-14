def fun(a, b, c, d):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)

fun(10, 20, c=30, d=40)
#fun(10, 20, a=30, c=30, d=40) #10已经对应了形参a，后续不能再对形参a赋值
print(list(range(0,3)))

lst = list(range(3))
print(lst)

lst1 = range(4)
print(type(lst1)) #range类型

num = 12
# print("num:" + num) #不同类型不可用字符串拼接，要全部转换为str类型才可拼接
print("num:" + str(num))
