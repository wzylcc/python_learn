#!/usr/bin/env python
# coding: utf-8

import codecs
import os

# write file
f = codecs.open('file_ch.txt', 'w', 'utf-8')
f.write(u'用Python做点事')
f.write(u'固态U盘')
f.write(u'我的博客')
f.close()

# read file
f = codecs.open('file_ch.txt', 'r', 'utf-8')
print f.readline()
print f.readline()
print f.readline()

# os path
print os.path.exists('file_ch.txt')
os.rename('file_ch.txt', 'file_test.txt')
print os.path.exists('file_ch.txt')
