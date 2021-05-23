#!/usr/bin/env python3

from heltal import Heltal
from time import perf_counter as pc
from time import sleep as pause
import matplotlib.pyplot as plt

def main():
	pyTimeY = []
	cppTimeY = []
	X = []

	for n in range(30, 45):
		f = Heltal(n)
		start = pc()
		x = f.fib()
		end = pc()
		cppTimeY.append(round(end-start, 2))
		X.append(n)
	print('Done C++')

	for n in range(30, 45):
		start = pc()
		d = fib_py(n)
		end = pc()
		pyTimeY.append(round(end-start, 2))
	print('Done Py')

	plt.plot(X, cppTimeY, label='C++')
	plt.plot(X, pyTimeY, label='Python')
	plt.legend()
	plt.savefig('fibTimeTest.png')

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

# C++ took 0.16 sec on 35 and Python took 4.55 on 35
# C++ is 28.45 times faster

if __name__ == '__main__':
	main()