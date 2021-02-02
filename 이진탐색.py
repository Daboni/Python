# 이진 탐색, binsect

# 이진 탐색 알고리즘(binary search)
# 오름차순으로 정렬된 리스트에서 특정 값의 위치를 찾는 알고리즘

# ex) 5를 찾는 알고리즘 구현

# 이진 탐색을 사용하지 않고 구현

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
for i in range(len(nums))):
    if n <= nums[i]:
        break

result = i
print(result)       # 5


# 이진 탐색을 사용하여 구현

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
l = 0
r = len(nums)-1
result = 0
while l<=r:
    mid = (l+r)//2
    if nums[mid]<n:
        r = mid-1
    else:
        result = mid
        l = mid+1

print(result)       # 5


# bisect를 사용하여 구현

import bisect

nums = [0,1,2,3,4,5,6,7,8,9]

result = bisect.bisect_left(nums,5)

print(result)       # 5
