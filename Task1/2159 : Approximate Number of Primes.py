import math
num = int(input())
if num >= 17 :
    p = num / math.log(num)
    m = 1.25506 * p  
    print(round(p,1)," ",round(m,1))
