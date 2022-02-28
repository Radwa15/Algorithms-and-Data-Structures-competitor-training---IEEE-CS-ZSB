d=int(input())
n=int(input())
r=0
l = map(int,input().split())
for x in l:
    r+=d-x
print(r-d+x)
