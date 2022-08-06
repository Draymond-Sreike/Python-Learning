# print(type(input("请输入")))

'''answer = input("您是会员吗？y/n")
if answer == 'y' :
    print("会员")
else :
    print("非会员")
'''

'''
num_a = int(input("请输入第一个数"))
num_b = int(input("请输入第二个数"))
#print( (num_a,'大于等于',num_b) if num_a >= num_b else num_a,'小于',num_b )
print( str(num_a)+'大于等于'+str(num_b) if num_a >= num_b else str(num_a)+'小于'+str(num_b) )
'''

for i in range(1, 10) :
    for j in range(1, i+1) :
        print(i, '*', j, '=', i*j, end='\t')
    print()
