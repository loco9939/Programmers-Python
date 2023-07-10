def solution(numLog):
    answer = ''
    logElem = numLog[0]
    for i in range(1,len(numLog)):
        if (logElem - numLog[i] == -1):
            answer += 'w'
        elif (logElem - numLog[i] == 1):
            answer += 's'
        elif (logElem - numLog[i] == -10):
            answer += 'd'
        else:
            answer += 'a'
        logElem = numLog[i]
    return answer