# 1.주요 함수

# addtoFirst() : 연결 리스트의 앞쪽에 원소를 추가하는 연산
# addtoLast() : 연결 리스트의 뒤쪽에 원소를 추가하는 연산
# get() : 연결 리스트의 특정 위치에 있는 원소를 리턴하는 연산
# add() : 연결 리스트의 특정 위치에 원소를 추가하는 연산
# delete() : 연결 리스트의 특정 위치에 원소를 삭제하는 연산

# 노드 : 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료단위
# 데이터 필드 : 원소의 값을 저장하는 자료구조
# 링크 필드 : 다음 노드의 주소를 저장하는 자료구조

# 헤드 : 리스트의 처음 노드를 가리키는 레퍼런스

# 단순 연결 리스트 : 노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조를 가짐
# 헤드가 가장 앞의 노드를 가리키고, 각 노드의 링크 필드가 연속적으로 다음 노드를 가리킴
# 최종적으로 None을 가리키는 노드가 리스트의 가장 마지막 노드임

# 단순 연결 리스트의 삽입 연산
# 1. 메모리를 할당하여 새로운 노드 new 생성
# 2. 새로운 노드 new의 데이터 필드에 'B' 저장
# 3. 삽입될 위치의 바로 앞에 위치한 노드의 링크 필드를 new에 복사
# 4. new의 주소를 앞 노드의 링크 필드에 저장

# 첫 번째 노드로 삽입하는 알고리즘
def addtoFirst(data):   # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)     # 새로운 노드 생성

# 가운데 노드로 삽입하는 알고리즘
def add(pre, data):     # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

# 마지막 노드로 삽입하는 알고리즘
def addtoLast(data):
    global Head
    if Head == None:    # 빈 리스트이면 바로 삽입
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:   # 마지막 노드 찾을 때까지
            p = p.link
        p.link = Node(data, None)

# 단순연결 리스트의 삭제 연산
# 1. 삭제할 노드의 앞 노드(선행노드) 탐색
# 2. 삭제할 노드의 링크 필드를 선행노드의 링크 필드에 복사

# 첫 번째 노드를 삭제하는 알고리즘
def deletetoFirst():    # 처음 노드 삭제
    global Head
    if Head == None:
        print('error')
    else:
        Head = Head.link

# 노드 pre의 다음 위치에 있는 노드 삭제
def delete(pre):    # pre 다음 노드 삭제
    if pre == None of pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

# 이중 연결 리스트
# 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
# 두 개의 링크 필드와 한 개의 데이터 필드로 구성

# cur이 가리키는 노드 다음에 D값을 가진 노드를 삽입하는 과정
# 1. 메모리를 할당하여 새로운 노드 new를 생성하고 데이터 필드에 'D'를 저장
# 2. cur의 next를 new의 next에 저장하여 cur의 다음 노드를 삽입할 노드의 다음 노드로 연결
# 3. new의 값을 cur의 next에 저장하여 삽입할 노드를 cur의 다음 노드로 연결
# 4. cur의 값을 new 의 prev 필드에 저장하여 cur를 new의 이전 노드로 연결
# 5. new의 값을 new가 가리키는 노드의 다음 노드의 prev필드에 저장하여 삽입하려는 
#    노드의 다음 노드와 삽입하려는 노드를 연결

# cur이 가리키는 노드를 삭제하는 과정
# 1. 삭제할 노드의 다음 노드의 주소를 삭제할 노드의 이전 노드의 next 필드에 저장하여 
#    링크를 연결
# 2. 삭제할 노드의 다음 노드의 prev 필드에 삭제할 노드의 이전 노드의 주소를 저장하여
#    링크를 연결
# 3. cur이 가리키는 노드에 할당된 메모리를 반환
