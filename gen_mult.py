import sys

sys.stdout = open('mult_test.txt', 'w')

N = 1000

print('w_0 0 0 T N')
for i in range(N+1):
    print('r1_{} 1 1 r1_{} R'.format(i, i+1))
    print('r1_{} 0 0 r2_{}_{} R'.format(i, i, 0))
    

for i in range(1, N+1):
    for j in range(N+1):
        print('r2_{}_{} 1 1 r2_{}_{} R'.format(i, j, i, (j+1)))
        print('r2_{}_{} 0 0 w_{} R'.format(i, j, i*j))

for i in range(1, N**2+1):
    print('w_{} 0 1 w_{} R'.format(i, i-1))
print('done')
print(0)
print('r1_0')
print('T')
sys.stdout.close()
