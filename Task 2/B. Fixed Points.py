n=int(input())
c=0
t=0
a=list(map(int,input().split()))
for i in range(n):
 if a[i]==i:
  c+=1
 elif i==a[a[i]]:
  t=1
print(c+t+int(c!=n))
