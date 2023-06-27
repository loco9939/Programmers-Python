def solution(my_string, alp):
    answer = ''
    for i in range(0, len(my_string)):
        if (my_string[i] == alp):
            answer += my_string[i].upper()
        else:
            answer += my_string[i]
    return answer