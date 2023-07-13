def solution(names):
    answer = []
    MAX_LINE = 5
    total_length = len(names)
    index = 0
    while (index < total_length):
        answer.append(names[index])
        index += MAX_LINE
    return answer