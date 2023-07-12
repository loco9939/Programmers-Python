def solution(a, b, c, d):
    answer = 0
    
    # 1~6까지 숫자가 몇개인지 세어서 obj에 dictionary로 할당
    arr = [a,b,c,d]
    obj = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in arr:
        if (i == 1):
            obj[1] += 1
        elif (i == 2):
            obj[2] += 1
        elif (i == 3):
            obj[3] += 1
        elif (i == 4):
            obj[4] += 1
        elif (i == 5):
            obj[5] += 1
        else:
            obj[6] += 1
    
    # 갯수가 0인 주사위는 제외하여 dices 리스트에 할당
    dices = []
    for key in obj:
        if (obj[key] != 0):
            dices.append(key)
    
    # dices의 길이에 따라 조건분기
    if (len(dices) == 1):
        answer = 1111 * dices[0]
    elif (len(dices) == 2):
        if (obj[dices[0]] == obj[dices[1]]):
            answer = (dices[0]+dices[1])*abs(dices[0] - dices[1])
        elif (obj[dices[0]] > obj[dices[1]]):
            answer = (10*dices[0]+dices[1])**2
        else:
            answer = (10*dices[1]+dices[0])**2
    elif (len(dices) == 3):
        if (obj[dices[0]] != 1):
            answer = dices[1] * dices[2]
        elif (obj[dices[1]] != 1):
            answer = dices[0] * dices[2]
        else:
            answer = dices[0] * dices[1]
    else:
        answer = min(a,b,c,d)    
    return answer