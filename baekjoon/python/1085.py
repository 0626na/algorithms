'''
백준 알고리즘 사이트 코딩테스트 연습문제 1085번 풀이코드

1. 주어진 위치의 각 x좌표와 y좌표를 꼭짓점 좌표의 x축 y축에서 뺀다. 이렇게 하면 x,y축에서 오른쪽 위 좌표를 기준으로 하는 오른쪽 변과 위쪽변까지의 거리를 구할수 있다.
2. 왼쪽변, 아랫변, 오른쪽변, 위쪽변으로 이동하는 각각의 거리중에 가장 작은 거리에 해당하는 값을 고른다. 이를 위해서 리스트에 넣고 오름차순으로 정렬한다.
'''

nums=list(map(int,input().split()))

x=nums[0]
y=nums[1]
w=nums[2]
h=nums[3]

xDistance=w-x
yDistance=h-y

arr=[x,y,xDistance,yDistance]
result=sorted(arr)

print(result[0])