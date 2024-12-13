'''
백준 알고리즘 사이트 코딩테스트 연습문제 1264번 풀이코드
'''

sentences:list[str]=[]

while 1:
    sentence=input()
    if(sentence=='#'):
        break
    sentences.append(sentence)


for text in sentences:
    lowerText=text.lower()
    
    count=0
    count+=lowerText.count('a')
    count+=lowerText.count('e')
    count+=lowerText.count('i')
    count+=lowerText.count('o')
    count+=lowerText.count('u')
    
    print(count)
