def solution(arr, queries):
    answer = []
    
    for query in queries:
        s,e,k = query
        k_arr = 1_000_000
        for i in range(len(arr)):
            if (s <= i and i <= e and arr[i] > k):
                if (k < arr[i]):
                    k_arr = arr[i]
        if (k_arr == 1_000_000):
            k_arr = -1
        answer.append(k_arr)
    return answer

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(arr,queries))