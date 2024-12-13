'''
백준 알고리즘 사이트 코딩테스트 연습문제 2845번 풀이코드
'''

nums=list(map(int,input().split()))
news=list(map(int,input().split()))
result=[]

people=nums[0]
partyPlace=nums[1]
partyPeople=people*partyPlace

for new in news:
    result.append(new-partyPeople)

print(' '.join(map(str,result)))