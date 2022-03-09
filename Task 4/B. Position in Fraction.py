a,b,c = map(int, input().split())
for i in range(b):
  a *= 10
  if a // b == c:
    print(i+1)
    break
  a %= b
else: 
  print(-1)
