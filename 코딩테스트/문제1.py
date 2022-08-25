def solution(lottos, win_nums):
    answer = []
    # lottos : 민우가 선택한 번호들
    # win_nums : 당첨번호
    
    # 내가 생각한 알고리즘 ??
    # 로또번호를 하나하나씩 당첨 번호와 비교한다.
    cor_num = 0
    zero_num = 0
    for lotto in lottos :
        # 비교할 때 로또번호가 0이면, 별도로 처리한다.
        if lotto == 0 :
            zero_num += 1 
            # 로또번호가 지워진 경우도 몇 개인지 알고 있어야한다. (변수로 저장한다.)
        else :
            if lotto in win_nums :
                cor_num += 1
                # 몇 개 맞췄는지 알고 있어야 한다.(변수로 저장한다.)
    
    
    # 맞춘 갯수와 지워진 갯수를 가지고 최대, 최소 몇개 맞출 수 있는지 확인한다. 
    max1  = cor_num + zero_num
    
    # 최대 맞춘 갯수와 최소로 맞춘 갯수로 순위를 확인한다. 
    bestrank = min(7 - max1, 6)
    worstrandk = min(7-cor_num,6)
    answer.append(bestrank)
    answer.append(worstrandk)
    
    return answer 

# def solution(lottos, win_nums):
#     answer = []
#     count_zero = 0
#     correct_num = 0
#     for i in lottos:
#         if i != 0:
#             if i in win_nums:
#                 correct_num += 1
#         else :
#             count_zero += 1
#     max_output = correct_num + count_zero
#     if max_output == 6:
#         answer.append(1)
#     elif max_output == 5:
#         answer.append(2)
#     elif max_output == 4:
#         answer.append(3)
#     elif max_output == 3:
#         answer.append(4)
#     elif max_output == 2:
#         answer.append(5)
#     else : 
#         answer.append(6)
        
#     if correct_num == 6:
#         answer.append(1)
#     elif correct_num == 5:
#         answer.append(2)
#     elif correct_num == 4:
#         answer.append(3)
#     elif correct_num == 3:
#         answer.append(4)
#     elif correct_num == 2:
#         answer.append(5)
#     else : 
#         answer.append(6)
        
    
#     return answer