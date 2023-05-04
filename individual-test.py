from time import time
import random
import copy

random.seed(0)


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
n = 20
trials = 10
print("Matrix size is %d-by-%d" % (n,n))

init_rand(A,n)
init_rand(B,n)
init_matrix(C,n,0)

record1 = open("ijk.txt","w+")

for x in range(trials):
    ctmp = copy.deepcopy(C) #changes in original array wont affect ctmp
    t = time()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("ijk completed in %f seconds" % (runtime))
    record1.write(f"{runtime}\n")
    fill_zero(C,n)
record1.close()
  
record2 = open("kji.txt","w+")
for x in range(trials):
    ctmp = copy.deepcopy(C)
    t = time()
    for k in range(n):
        for j in range(n):
            for i in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("kji completed in %f seconds" % (runtime))
    record2.write(f"{runtime}\n")
    fill_zero(C,n)
record2.close()

record3 = open("jik.txt","w+")
for x in range(trials):
    ctmp = copy.deepcopy(C)
    t = time()
    for j in range(n):
        for i in range(n):
            for k in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("jik completed in %f seconds" % (runtime))
    record3.write(f"{runtime}\n")
    fill_zero(C,n)
record3.close()

record4 = open("jki.txt","w+")
for x in range(trials):
    ctmp = copy.deepcopy(C)
    t = time()
    for j in range(n):
        for k in range(n):
            for i in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("jki completed in %f seconds" % (runtime))
    record4.write(f"{runtime}\n")
    fill_zero(C,n)
record4.close()

record5 = open("kij.txt","w+")
for x in range(trials):
    ctmp = copy.deepcopy(C)
    t = time()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("kij completed in %f seconds" % (runtime))
    record5.write(f"{runtime}\n")
    fill_zero(C,n)
record5.close()

record6 = open("ikj.txt","w+")
for x in range(trials):
    ctmp = copy.deepcopy(C)
    t = time()
    for i in range(n):
        for k in range(n):
            for j in range(n):
                ctmp[i][j] = ctmp[i][j] + A[i][k]*B[k][j]
    runtime = time() - t
    print("ikj completed in %f seconds" % (runtime))
    record6.write(f"{runtime}\n")
    fill_zero(C,n)
record6.close()

