s = 6
arr = [1, 4, 3, 1, 5]

def solution(arr,s):
    left,sum = 0,0
    for right in range(len(arr)):
        sum += arr[right]
        while (left < right and sum > s):
            sum -= arr[left]
            left += 1
        if sum == s:
            return [left+1,right+1]
    return [-1]

print(solution(arr,s))