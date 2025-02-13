from main import *
import math


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(1, 4, 2) == 1
	assert simple_work_calc(30, 4, 3) == 182
	assert simple_work_calc(40, 4, 2) == 2136


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 11
	assert work_calc(20, 1, 2, lambda n: n * n) == 527
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(20, 3, 2, lambda n: n + n) == 244
	assert work_calc(1, 3, 2, lambda n: n**(n**n)) == 1
	assert work_calc(30, 3, 2, lambda n: n + 1) == 340

	


def test_compare_work(n):
	#curry work_calc to create multiple work
	#functions taht can be passed to compare_work
	work_fn1 = (n * n)
	work_fn2 = (math.log(n))
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	print(compare_work(work_fn1, work_fn2, sizes))


#def test_compare_span():

work_fn1 = (n * n)
work_fn2 = (math.log(n))
sizes = [10, 20, 50, 100, 1000, 5000, 10000]
print(compare_span(work_fn1, work_fn2, sizes))
