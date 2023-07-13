def solution(numbers, n):
    answer = 0
    index = 0
    while (answer <= n):
        answer += numbers[index]
        index += 1
    return answer