x = 7
i = 1
m = 0
while i <= 200:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6 == 5):
        m = 1
        break
    else:
        x = 7*(i + 1)   
    i += 1
if m == 1:
    print("阶梯数是：", x)
else:
    print("在程序限定范围内找不到答案！")
