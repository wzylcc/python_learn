#!/usr/bin/env python
# coding: utf-8

import shelve
f = shelve.open('file_test.shelve')
f['google'] = 'www.google.com'
f['taobao'] = 'www.taobao.com'
f['163'] = 'www.163.com'

print f
f.close()
g = shelve.open('file_test.shelve')
print g

print "----------------------------------------"
import cPickle
f = open('file_test.pkl', 'w')

obj1 = 2015,"lavenliu",[1,2,3,4],{"python":1998,"java":1995}
obj2 = ['heibanke', 'junminl1', 'lavenliu', 'sjtu']

cPickle.dump(obj1, f)
cPickle.dump(obj2, f)

f.close()

# read file
f = open('file_test.pkl', 'r')
obj1_r = cPickle.load(f)
print obj1_r

obj2_r = cPickle.load(f)
print obj2_r
f.close()
