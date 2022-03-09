n,k,t=map(int,input().split())
t=(n*k*t)//100
for i in range(n):
  print(min(max(0,t-i*k),k),end=' ')
