n,a,b,c,t=map(int,input().split())
s=sum(map(int,input().split()))
print(max(a*n-(t*n-s)*b+(n*t-s)*c,a*n))
