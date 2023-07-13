def solution(my_string):
    answer = []
    trimmed = my_string.strip()
    stack = ''
    for i in range(len(trimmed)-1):
        if (trimmed[i] != ' ' and trimmed[i+1] == ' '):
            stack += trimmed[i]
            answer.append(stack)
            stack = ''
        elif (trimmed[i] != ' ' and trimmed[i+1] != ' '):
            stack += trimmed[i]
    
    if (trimmed[len(trimmed) - 1] != ' '):
        stack += trimmed[len(trimmed) - 1]
        answer.append(stack)
    
    return answer

# answer = my_string.split() 으로 간단히 해결 가능