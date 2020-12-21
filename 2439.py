N = int(input())


for i in range(1,N+1):
  if(i!=1):
    print("")
  for k in range(N-i,0,-1):
    print(' ',end='')
  for j in range(0,i):
    print('*',end='')
    