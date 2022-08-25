def solution(n):
    # 3진법
    # 3으로 계속 나눠서 몫이 0일떄까지 나오게 한다음에 이어줌
    answer = ''
    # 3진법
    number_dict = {
        1 : '1',
        2 : '2',
        0 : '4'
    }
    while n != 0 :
        나머지 = n % 3 
        answer = number_dict[나머지] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else : 
            n = n // 3
    return answer


# def solution(n):
#     answer = ''
#     if n < 4 :
#         return str(2**(n-1))
#     if n % 3 != 0:
#         answer = solution(n//3) + solution(n%3)
#     else : 
#         answer = solution(n//3-1) + solution(3)
#     return answer