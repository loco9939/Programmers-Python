def solution(myString):
    answer = []
    stack = ''
    
    for i in range(len(myString)):
        if (myString[i] != 'x'):
            stack += myString[i]
        else:
            if (stack == ''):
                continue
            answer.append(stack)
            stack = ''
    if (stack != ''):
        answer.append(stack)
    return sorted(answer)

myString = 'axxbxc'
print(solution(myString))