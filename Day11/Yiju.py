def solution(arr, queries):
    answer = []
    
    for query in queries:
        s,e,k = query
        k_min = 1_000_000
        for i in range(len(arr)):
            if (s <= i and i <= e and arr[i] > k):
                if (k_min > arr[i]):
                    k_min = arr[i]
        if (k_min == 1_000_000):
            k_min = -1
        answer.append(k_min)
    return answer