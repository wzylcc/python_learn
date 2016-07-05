#!/usr/bin/env python3

#读取文件并转换为字典
PasswdFileR = open('passwd','r')
Dict=PasswdFileR.readlines()
PasswdFileR.close()
Passwd = eval(Dict[0].strip('\n'))
Lock = eval(Dict[1])

Username = input('Username:')

#循环3次和判断
for i in range(3):
    Password = input('Password:')
    #判断账户是否锁住
    if Lock[Username] != 0:
        print('User %s is locked!' %Username)
        break
    #判断用户名密码是否正确
    elif Passwd.get(Username)==Password:
        print('login!')
        break
    else:
        print('password or username is wrong!')
        #判断是否是最后一次验证，并对账户加锁
        if i==2:
            print('User %s is locked!' %Username)
            Lock[Username] = 1
            PasswdFileW = open('passwd', 'w')
            PasswdFileW.write(str(Passwd).strip() + "\n")
            PasswdFileW.write(str(Lock))
            PasswdFileW.close()
