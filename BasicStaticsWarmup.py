import math

N = int(input())
arr = []
l = []
l = input()
arr = list(map(int, l.split()))
arr.sort()

#Calulate Mean
mean = sum(arr)/ N
print("%.1f" %(mean))

#Calulcate median
if N % 2 == 0:
    median = (arr[int(N/2)] + arr[int(N/2)-1])/2
else:
    median = arr[int(N/2)]
print("%.1f" %(median))

#Calculate Mode
mode = max(arr,key=arr.count)
print(mode)


#Calculate Standard deviation
sum_result = 0
for x in arr:
    sum_result += pow((x - mean),2)

sd = pow((sum_result / N), 0.5)
print("%.1f" %(sd))

#Calculate Confidence Interval for the mean,
sd_error_mean = sd / math.sqrt(N)

lower_boundary = mean - 1.96 * sd_error_mean
upper_boundary = mean + 1.96 * sd_error_mean
print("%.1f %.1f" %(lower_boundary, upper_boundary))
