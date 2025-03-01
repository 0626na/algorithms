"""
그래프를 2차원 배열로 표현하는 방식
그래프의 노드간의 연결관계를 2차원 배열에 전부 표현한다.
파이썬에서는 array 형식의 데이터 구조를 리스트라고 부르기에 헷갈릴수 있다. 

0 1 2 라는 세개의 노드가 존재하고 0만이 1과 2에 연결된 화살표 형식의 그래프라고 가정할때 이 그래프를 2차원리스트로 구현
"""

NOT = 99999  # 연결되어 있지 않는 노드간의 관계일때 표현


graph = [
    # 2차원 리스트이기에 0에 해당하는 첫번째 인덱스가 노드를 표시하고 안의 세개의 갚들은 현재 노드인 0과 0, 1, 2 이 세가지 노드의 관계를 표시
    # 맨앞의 0은 자기 자신이기에 간선이 0, 두번째인 1은 노드 1과의 간선이 7만큼 있고 노드 2와의 간선이 5 만큼 있음을 나타낸다.
    [0, 7, 5],
    # 두번째 리스트가 있는 데는 노드 1의 연결관계를 나타낸다. 맨앞의 0은 노드0과의 관계 이므로 간선 7, 두번째인 1은 자기자신이기에 0, 세번째인 2는 노드 2와는 연결되어 있지 않기에 연결이 없다라는 NOT을 넣어준다.
    [7, 0, NOT],
    # 세번째 리스트는 노드 2의 그래프 연결관계를 나타낸다. 맨앞은 노드 0과의 관계이므로 간선 5, 두번째는 노드 1과의 관계인데 노드 1과는 연결이 없으므로 NOT, 세번째 2는 자기자신이기에 0이 들어간다.
    [5, NOT, 0],
]
