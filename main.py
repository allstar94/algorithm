N, X = map(int, input().split())


num_list = list(map(int, input().split()))

for i in range(0,N):
  if(num_list[i] < X):
    print(num_list[i],end = ' ')