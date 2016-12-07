'''
Pearson’s Correlation Coefficients

To know more about Pearson's Correlation Coefficients, refer to
http://www.statisticshowto.com/how-to-compute-pearsons-correlation-coefficients/

'''

import numpy

def pearson(x, y):
    n = len(x)
    
    sum_x = float(sum(x))
    sum_y = float(sum(y))
    
    sum_sq_x = sum(map(lambda x : pow(x, 2), x))
    sum_sq_y = sum(map(lambda y : pow(y, 2), y))
    
    sum_xy = sum(map(lambda x, y : x * y, x, y))
    
    num = n * sum_xy - sum_x * sum_y
    
    den = pow(((n * sum_sq_x) - pow(sum_x, 2)), 0.5 ) * pow(((n * sum_sq_y) - pow(sum_y, 2)), 0.5)
    
    if(den == 0):
        return 0
    
    return num / den

s = input()
s = list(map(int, s.split()))

l = s.index(len(s)/2)
x = s[:l]
y = s[l:]

a = pearson(x, y)
print("%.3f" %(a))
