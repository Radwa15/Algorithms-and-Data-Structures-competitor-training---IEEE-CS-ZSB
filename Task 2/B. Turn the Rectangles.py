n=int(input())
x=10**9
for i in range(0,n):
 w,h=sorted(map(int,input().split()))
 if h<=x:
     x=h
 elif w<=x:
     x=w
 else:
     print('NO')
     exit()
print('YES')
