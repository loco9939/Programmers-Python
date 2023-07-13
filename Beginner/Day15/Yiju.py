def solution(arr):
    answer = 0
    nums = 0
    prev = []
    arr_x = [x for x in arr]
    while True:
        prev = [x for x in arr_x]
        # arr_x에 조건대로 할당
        for j in range(len(arr_x)):
            if (arr_x[j] >= 50 and arr_x[j] % 2 == 0):
                arr_x[j] = int(arr_x[j] / 2)
            elif (arr_x[j] < 50 and arr_x[j] % 2 != 0):
                arr_x[j] = arr_x[j] * 2 + 1
                
        # arr_x와 이전 배열을 비교
        for i in range(len(arr_x)):
            if (arr_x[i] == prev[i]):
                nums += 1
                
        if (nums == len(arr_x)):
            break
        nums = 0
        answer += 1
    return answer