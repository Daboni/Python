# heap, priority queue

# 파이썬은 heapq 내장 모듈로 heap을 구현할 수 있음

# min heap에서 가장 작은 값은 언제나 인덱스가 0, 즉 이진 트리의 루트에 위치
# heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

import heapq

# heap 생성
heap = []

# 원소 추가
heapq.heappush(heap,3)
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)

print(heap)

#원소 삭제
print(heapq.heappop(heap))
print(heap)

print(heapq.heappop(heap))
print(heap)

# 최소값 얻기
print(heap[0])

# 리스트 힙 변환
heap = [1,2,3,4,5,6,7]
heapq.heapify(heap)
print(heap)

# Max heap
num = [1,2,3,4,5,6,7]
heap = []

for n in num:
    heapq.heappush(heap,(-n,n))

while heap:
    print(heapq.heappop(heap)[1])

# 응용 - 힙 정렬

import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap,num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

print(heap_sort([1,3,2,6,4,8]))
