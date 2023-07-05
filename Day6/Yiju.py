def solution(num_list):
    answer = sorted(num_list)[:5]
    return answer

term = 10

result = list(map(lambda x,y: x+y, range(term)))

for i in range(term):
    print('2 raised to power', i, 'is', result[i])