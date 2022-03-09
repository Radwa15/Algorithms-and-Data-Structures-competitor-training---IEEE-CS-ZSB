n = int(input()) 
a = list(map(int, input().split()))
t=min(a)
while a[t%n] > t:
         t+=1
print( t%n + 1 )
