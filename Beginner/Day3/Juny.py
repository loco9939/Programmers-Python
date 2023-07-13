def solution(numbers, n):
    answer = 0

    for num in numbers:
        if answer > n:
            return answer
        else:
            answer += num

    return answer
