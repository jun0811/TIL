# 병합정렬
# 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
# 1. 분할 정복 알고리즘 활용
#  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
#  - Top-Down 방식
# 2. 시간 복잡도 : O(n lon n)

# {69, 10, 30, 2, 16, 8, 31, 22}를 병합 정렬하는 과정
# 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속함
# 위의 집합을 크기가 1인 부분집합이 될때까지 분할하는 작업
# ex) {69}, {10}, {30}, {2}, {16}, {8}, {31}, {22}
# 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
# ex) 8개의 부분집합이 1개로 병합될 때까지 반복함


# 분할 과정의 알고리즘
def merge_sort(m):
    if len(m) <= 1:     # 사이즈가 0이거나 1인 경우, 바로 리턴
        return m

    # 1. Divide 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right) 

    # 2. Conquer 부분 : 분할된 리스트들 병합
    return merge(left, right)


# 병합 과정의 알고리즘
def merge(left, right):
    result = []    # 두 개의 분할된 리스트를 병합하여 result를 만듦

    while len(left) > 0 and len(rigth) > 0:    # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:    # 왼쪽 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0:   # 오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result