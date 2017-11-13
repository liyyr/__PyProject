#! coding:utf-8


#输入两个数字，比较大小，按升序方式排列

stop = 1
while(stop):
    a = input("请输入a的数值：")
    b = input("请输入b的数值：")
    
    if int(a)<int(b):
        print(a,b)
    elif int(a)>int(b):
        print(b,a)
    else:
        print("两个数字相等")

    try:
        stop = int(input("按0退出，任意键继续："))
    except:
        stop = 1