#!/usr/bin/env python3
#读取文件并转换成字典
PasswdFileR = open('passwd','r')
Dict=PasswdFileR.readlines()
PasswdFileR.close()
Passwd = eval(Dict[0].strip('\n'))
Lock = eval(Dict[1])
#输入用户名和密码，如果已有的用户可以解锁
Username = input('Username:')
Password = input('Password:')
Passwd[Username] = Password
Lock[Username] = 0
PasswdFileW = open('passwd','w')
PasswdFileW.write(str(Passwd).strip()+"\n")
PasswdFileW.write(str(Lock))
PasswdFileW.close()
