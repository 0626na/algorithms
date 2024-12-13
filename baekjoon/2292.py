
'''
수학의 등차수열 개념을 알아야 풀수있다.
'''
num=int(input())
floor=2

while 1:
   rooms=1 + 6 * floor * (floor-1)/2
   if(num<=rooms):
       break
   floor+=1

if(num==1):
    print(1)
else:
    print(floor) 