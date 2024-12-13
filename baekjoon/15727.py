'''
백준 알고리즘 사이트 코딩테스트 연습문제 15727번 풀이코드
'''

distance=int(input())
    
if(distance%5==0):
    print(distance//5)
else:
    print(distance//5+1)