import numpy

'''
Pearson coefficient correlation between two lines
'''
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

'''
Mean of a list
'''
def mean(X, N):
    Mean = sum(X)/N
    return Mean

'''
Standarad deviation of a list
'''
def Standard_deviation(X, N):
    sum_result = 0
    Mean = mean(X, N)
    for i in X:
        sum_result += pow((i - Mean), 2)

    sd = pow((sum_result / N), 0.5)
    return sd


s = input()
s = list(map(int, s.split()))

l = s.index(len(s)/2)
x = s[:l]
y = s[l:]

Mx = mean(x,l)
My = mean(y,l)
Sx = Standard_deviation(x, l)
Sy = Standard_deviation(y, l)
r = pearson(x, y)

print(type(Mx))
print(type(My))
print(type(Sx))
print(type(Sy))
print(type(r))
slope = float(r *(Sy/Sx))
print("%.3f"%slope)
