#!/usr/bin/env python3

#init list and dict
L1=['a','b','c']
D1={'a':['aa','ab','ac'],'b':['ba','bb','bc'],'c':['ca','cb','cc'],'aa':['aaa','aab','aac'],'ab':['aba','abb','abc'],'ac':['aca','acb','acc'],'ba':['baa','bab','bac'],'bb':['bba','bbb','bbc'],'bc':['bca','bcb','bcc'],'ca':['caa','cab','cac'],'cb':['cba','cbb','cbc'],'cc':['cca','ccb','ccc'],}
i = 0

#通过i变量做while循环判断菜单等级状态
while i <3:
    #1级菜单，利用L1实现选择
    if i == 0:
        print("1.%s 2.%s 3.%s" %(L1[0],L1[1],L1[2]))
        M1=input("please choose(q is quit):\n")
        if M1=='q':
            break
        #判断是否不是字符串格式
        elif not str.isdigit(M1):
            print("wrong input!!")
            continue
        N1= L1[int(M1)-1]
        print('%s' %N1)
        i+=1
    else:
        #利用1级菜单遗留的参数实施对2级和3级菜单的控制。
        if i==1:
            L2 = D1[N1]
        else:
            L2 = D1[N2]
        print("1.%s 2.%s 3.%s" %(L2[0],L2[1],L2[2]))
        M1 = input("please choose(q is quit，b is ):\n")
        if M1 == 'q':
            break
        #如果按b就返回上级菜单
        elif M1 == 'b':
            i-=1
            continue
        elif not str.isdigit(M1):
            print("wrong input!!")
            continue
        N2 = L2[int(M1) - 1]
        print('%s' %N2)
        i+=1
