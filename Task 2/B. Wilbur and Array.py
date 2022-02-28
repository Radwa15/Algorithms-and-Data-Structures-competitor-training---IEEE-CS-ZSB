n=int(input())
x=list(map(int,input().split()))
c=0
t=0
for i in x:
    c+=abs(t-i)
    t=i
print(c)
