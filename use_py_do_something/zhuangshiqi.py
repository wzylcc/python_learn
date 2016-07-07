#!/usr/bin/env python
# coding: utf-8


def outer(fun):
    def wrapper():
        print "Verify"
        fun()
        print "Welcome"
    return wrapper


@outer
def func1():
    print "func1"


@outer
def func2():
    print "func2"


@outer
def func3():
    print "func3"


@outer
def func4():
    print "func4"


func1()
func2()
func3()
func4()
