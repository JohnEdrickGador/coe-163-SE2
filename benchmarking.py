from time import time
import random
import copy

random.seed(0)

# #@title Matrix size (n-by-n)
# n = 10 #@param {type:"integer"}

n = 10

def init_rand(mat,n):
  for x in range(n):
    new = []
    for y in range(n):
      new.append(random.random())
    mat.append(new)

def init_matrix(mat,n,value):
  for x in range(n):
    new = []
    for y in range(n):
      new.append(value)
    mat.append(new)

def fill_zero(mat,n):
  for x in range(n):
    for y in range(n):
     mat[x][y] = 0

A = []
B = []
C = []
print("Matrix size is %d-by-%d" % (n,n))

init_rand(A,n)
init_rand(B,n)
init_matrix(C,n,0)

ctmp = copy.deepcopy(C) #changes in original array wont affect ctmp
t = time()
for i in range(n):
  for j in range(n):
    for k in range(n):
      ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("ijk completed in %f seconds" % (runtime))
fill_zero(C,n)

### PLEASE INPUT YOUR kji CODE HERE ###
ctmp = copy.deepcopy(C)
t = time()
for k in range(n):
  for j in range(n):
    for i in range(n):
      ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("kji completed in %f seconds" % (runtime))
fill_zero(C,n)

### PLEASE INPUT YOUR jik CODE HERE ###
ctmp = copy.deepcopy(C)
t = time()
for j in range(n):
    for i in range(n):
        for k in range(n):
            ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("jik completed in %f seconds" % (runtime))
fill_zero(C,n)

### PLEASE INPUT YOUR jki CODE HERE ###
ctmp = copy.deepcopy(C)
t = time()
for j in range(n):
    for k in range(n):
        for i in range(n):
            ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("jki completed in %f seconds" % (runtime))
fill_zero(C,n)

### PLEASE INPUT YOUR kij CODE HERE ###
ctmp = copy.deepcopy(C)
t = time()
for k in range(n):
    for i in range(n):
        for j in range(n):
            ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("kij completed in %f seconds" % (runtime))
fill_zero(C,n)


### PLEASE INPUT YOUR ikj CODE HERE ###
ctmp = copy.deepcopy(C)
t = time()
for i in range(n):
    for k in range(n):
        for j in range(n):
            ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("ikj completed in %f seconds" % (runtime))
fill_zero(C,n)

