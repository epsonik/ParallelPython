from __future__ import print_function
import math, sys, time, pp

def add(i, c, A, X):
	s=0
	s += A[i][c] * X[c][0]
	return s
def read(fname):
	f = open(fname, "r")
	nr = int(f.readline())
	nc = int(f.readline())

	A = [[0] * nc for x in xrange(nr)]
	r = 0
	c = 0
	for i in range(0,nr*nc):
		A[r][c] = float(f.readline())
		c += 1
		if c == nc:
			c = 0
			r += 1

	return A
def write(nrows, ncols, y):
    for i in range(nrows):
        for c in range(0, ncols):
            print (str(y[i*ncols+c]) + ' ', end='')
        print('\n')
ppservers = ()
ncpus = 2
job_server = pp.Server(ncpus, ppservers=ppservers)

start_time = time.time()

fnameA="A.dat"
fnameX="X.dat"

A = read(fnameA)
X = read(fnameX)
nrows = len(A)
ncols = len(A[0])
y = []
for i in range(nrows):
    for c in range(0, ncols):
        y.append((job_server.submit(add, (i, c, A, X)))())


write(nrows, ncols, y)