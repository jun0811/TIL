# 트리

# 트리의 개념
# 비선형 구조
# 원소들 간에 1:n 관계를 가지는 자료구조
# 원소들 간에 계층관계를 가지는 계층형 자료구조
# 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무) 모양의 구조

# 트리 - 정의
# 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
# - 노드 중 최상위 노드를 루트(root)라 한다.
# - 나머지 노드들은 n(>=0)개의 분리 집합 T1, T2, .... , TN으로 분리될 수 있다.
# 이들 T1, ... , TN 은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리 (subtree)라 한다.
# 단말 노드(터미널) : 자식이 없는 노드(leaf)
# 중간점(가지노드)
# 트리는 여러개의 부트리로 이루어져 있다.

# 트리 - 용어정리
# 노드(node) : 트리의 원소
# 간선(edge) : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
# 로트 노드(root node) : 트리의 시작 노드
# 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
# 차수(degree)
# - 노드의 차수 : 노드에 연결된 자식 노드의 수
# - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
# - 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드
# 높이
# - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
# - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
# 너비
# - 노드갯수

# 이진트리(Binary Tree)
# 트리의 특정 해
# 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
# 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리 (왼쪽자식노드, 오른쪽자식노드)

# 이진트리 - 특성
# 레벨 i에서의 노드의 최대 개수는 2^i 개
# 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는
# (2^(h+1)-1)개가 된다.

# 이진트리 - 종류
# 포화 이진 트리(Full Binary Tree)
# - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
# - 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
# - 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐(1차원 인덱스)

# 완전 이진 트리(Complete Binary Tree)
# - 높이가 h이고 노드 수가 n개일 때(단, h+1 <= n < 2^(h+1)-1), 포화 이진 트리의 노드
#   번호 1번 부터 n번까지 빈 자리가 없는 이진 트리
# 예) 노드가 10개인 완전 이진 트리

# 편향 이진 트리(Skewed Binary Tree)
# - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 바얗ㅇ의 자식 노드만을 가진 이진 트리
# ex) 왼쪽 편향 이진 트리, 오른쪽 편향 이진 트리(트리로서의 가치가 없음)

# 이진트리 - 순회(traversal)
# 순회란 트리의 각 노드를 중복되지 않게 전부 방문(visit) 하는 것을 말하는데
# 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
# 따라서 특별한 방법이 필요하다.
# 순회(traversal) : 트리의 노드들을 체계적으로 방문하는 것
# 3가지의 기본적인 순회방법
# 1. 전위순회(preorder traversal) : VLR
# - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.
# 2. 중위순회(inorder traversal) : LVR
# - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.
# 3. 후위순회(postorder traversal) : LRV
# - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.
# V(루트), L(왼쪽 서브트리), R(오른쪽 서브트리)

# 전위 순회
# 수행방법
# 1. 현재 노드 n을 방문하여 처리한다. -> V
# 2. 현재 노드 n의 왼쪽 서브트리로 이동한다. -> L
# 3. 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R
# 전위 순회 알고리즘
def preorder_traverse(T):   # 전위순회
    if T:      # T is not None
        visit(T)       # 방문처리가 아님(방문하라는 의미임)
        preorder_traverse(T.left)    # 재귀
        preorder_traverse(T.right)

# 중위 순회
# 수행방법
# 1. 현재 노드 n의 왼쪽 서브트리로 이동한다. -> L
# 2. 현재 노드 n을 방문하여 처리한다. -> V
# 3. 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R
# 중위 순회 알고리즘
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)

# 후위 순회
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)


# 이진트리의 표현 
# 배열을 이용한 이진 트리의 표현
# - 이진 트리에 각 노드 번호를 다음과 같이 부여
# - 루트의 번호를 1로 함
# - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^(n+1)-1까지 번호를 부여
# 배열을 이용한 이진 트리의표현
# 노드 번호의 성질
# - 노드 번호가 i인 노드의 부모 노드 번호? : i // 2
# - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호? : 2*i
# - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호? : 2*i + 1 
# - 레벨 n의 노드 번호 시작 번호는? : 2^n
# - 높이가 h인 이진 트리를 위한 배열의 크기는? : 2^(h+1)-1

# 배열을 이용한 이진 트리의 표현의 단점
# 편향 이진 트리의 경우에 사용하지 않는 배열 우너소에 대한 메모리 공간 낭비 발생
# 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경
# 어려워 비효율적

# 트리의 표현 - 연결리스트
# 배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를
# 표현할 수 있다.
# 연결 자료구조를 이용한 이진트리의 표현
# - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결
#   리스트 노드를 사용하여 구현 (left/ 데이터/ right)


# 연습문제
'''첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 "부모 자식" 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가
자식을 의미한다. 간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면
자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
- 13 (정점의 개수)
- 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회.py 참고


# 수식트리
# 수식을 표현하는 이진 트리
# 수식 이진 트리(Expression Binary Tree)라고 부르기도 함.
# 연산자는 루트 노드이거나 가지 노드
# 피연산자는 모두 잎 노드
# 후위순회로 풀어야함

# 이진 탐색 트리(BST)
# 탐색작업을 효율적으로 하기 위한 자료구조
# 모든 원소는 서로 다른 유일한 키를 갖는다.
# key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
# 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.
# 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

# 이진 탐색 트리 - 연산
# 탐색 연산
# - 루트에서 시작한다.
# - 탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
# - (x = 루트노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 탐색연산 성공
# - (x < 루트노드의 키 값)인 경우 : 루트노드의 왼쪽서브트리에 대해서 탐색연산 수행
# - (x > 루트노드의 키 값)인 경우 : 루트노드의 오른쪽 서브트리에 대해서 탐색연산
# 서브트리에 대해서 순환적으로 탐색 연산을 반복한다.

# 탐색연산
# 1. 먼저 탐색 연산을 수행
# 2. 탐색 실패한 위치에 원소를 삽입한다.

# 이진 탐색 트리 - 성능
# 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다.
# 평균의 경우 : 이진트리가 균형적으로 생성되어 있는 경우 : O(log n)
# 최악의 경우 : 한쪽으로 치우친 경사 이진트리의 경우 : O(n)
# 순차탐색과 시간복잡도가 같다.

# 이진 탐색 트리 - 연산 연습
# 삭제 연산
# 삭제

# 이진 탐색 트리 - 성능
# 검색 알고리즘의 비교
# 1. 배열에서의 순차 검색 : O(N)
# 2. 정렬된 배열에서의 순차 검색: O(N)
# 3. 정렬된 배열에서의 이진탐색 : O(logN)
# 4. 이진 탐색트리에서의 평균 : O(logN)
# 5. 해쉬 검색 : O(1)  -- B 형에서 배움

# 힙(heap) - 우선순위 큐 활용
# 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를
# 찾기 위해서 만든 자료구조

# 최대 힙(max heap)
# - 키 값이 가장 큰 노드를 찾기 위한 !!완전 이진 트리!!
# - {부모노드의 키값 > 자식노드의 키값}
# - 루트 노드 : 키값이 가장 큰 노드

# 최소 힙(min heap)
# - 키 값이 가장 작은 노드를 찾기 위한 !!완전 이진 트리!!
# - {부모노드의 키값 < 자식노드의 키값}
# 루트 노드 : 키값이 가장 작은 노드

# 힙 연산 - 삭제
# 힙에서는 루트 노드의 원소만을 삭제 할 수 있다.
# 루트 노드의 원소를 삭제하여 반환한다.
# 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.

# 최대힙을 계속 빼내서 출력하면 내림차순 정렬 : 힙정렬이라고 한다.
# 최소힙은 오름차순 : 힙정렬



# 최소힙 구현하기
# 최소힙.py 참고






 