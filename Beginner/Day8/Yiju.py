def solution(todo_list, finished):
    answer = []
    
    for i in range(len(finished)):
        if (not finished[i]):
            answer.append(todo_list[i])
    return answer