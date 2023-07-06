def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        s,e = parts[i]
        answer += (my_strings[i][s:e+1])
        
        
    return answer

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]

solution(my_strings,parts)