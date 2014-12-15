#!/usr/bin/env python
# coding:utf-8
# name = raw_input('Please enter your name: ');
# print 'hello', name;

# print absolute value of an integer
# a = int(raw_input('Please input a number: '));
# if a >= 0:
# 	print a;
# else:
# 	print -a;

# print '今天天气好晴朗'

# age = 20;
# if age >= 18:
# 	print 'your age is', age
# 	print 'adult'
# elif age >= 21:
# 	print 'your age is', age
# else:
# 	print 'You are too old'

# list and tuple
# classmates = ['Richard', 'Michael', 'Lucy']
# for name in classmates:
# 	print name

# sum = 0;
# for x in xrange(1,10):
# 	sum = sum + x;
# print sum;

# sum = 0
# for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
# 	sum = sum + x
# print sum

# sum = 0;
# for x in range(101):
# 	sum = sum + x
# print sum

# sum = 0
# for x in xrange(1,101):
# 	sum = sum + x
# print sum

# sum = 0
# n = 99
# while n > 0:
# 	sum = sum + n
# 	n = n - 2
# print sum

# def function my_abs()
# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('bad operand type')
# 	if x > 0:
# 		return x
# 	else:
# 		return -x

# a = int(raw_input('Please input the number: '))
# print my_abs(a)

# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi/2)
# print x, y

# def power(x, n):
# 	s = 1 
# 	while n > 0:
# 		n = n - 1
# 		s = s * x
# 	return s

# print power(5, 2)

# 可变参数
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n * n
# 	return sum
# print calc(1, 2, 3)

# 斐波那契数列
# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		print b
# 		a, b = b, a+b
# 		n = n + 1
# print fib(7)


# def log(func):
# 	def wrapper(*args, **kw):
# 		print 'call %s()' % func.__name__
# 		return func(*args, **kw)
# 	return wrapper
# @log
# def now():
# 	print '2014-12-12'
# now()

# 装饰器
# def log(text):
# 	def decorate(func):
# 		def wrapper(*args, **kw):
# 			print 'call %s %s()' % (text, func.__name__)
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorate
# @log('Nice')
# def now(today):
# 	print '%s is good day' % (today)
# now('Richard')

# import functools

# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print 'call %s():' % (func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
# @log
# def now():
# 	print '2014-12-12'
# now()
# print now.__name__

# try:
# 	print 'try...'
# 	r = 10 / 2
# 	print 'result:', r
# except ZeroDivisionError, e:
# 	print 'except:', e
# finally:
# 	print 'finally...'
# print 'END'

# with open('/Users/Richard/Documents/Project/Python/Study/test.txt', 'r') as f:
# 	for line in f.readlines():
# 		print(line.strip())

# multiprocessing
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end - start))

# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(10):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'


# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
# 	for value in ['A', 'B', 'C']:
# 		print 'Put %s to queue...' % value
# 		q.put(value)
# 		time.sleep(random.random())

# # 读数据进程执行的代码：
# def read(q):
# 	while True:
# 		value = q.get(True)
# 		print 'Get %s from queue' % value

# if __name__=='__main__':
# 	# 父进程创建Queue，并传递给各个子进程
# 	q = Queue
# 	pw = Process(target=write, args=(q,))
# 	pr = Process(target=read, args=(q,))
# 	# 启动子进程pw, 写入：
# 	pw.start()
# 	# 启动子进程pr，读取：
# 	pr.start()
# 	# 等待pw结束
# 	pw.join()
# 	# pr进程是死循环，无法等待其结束，强行终止：
# 	pr.terminate()

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()