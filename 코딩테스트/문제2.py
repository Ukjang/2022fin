def solution(id_list, report, k):
    answer = []
    
    # id_list = 유저목록 ( 유니크함 )
    # report = 신고 내역 ('신고자 신고당한자')
    # k = 정지 기준 횟수
    report_info = {}
    for user in id_list :
        report_info[user] = set()
        
    # 내가 생각한 알고리즘
    # 누가 신고 당했는지 알아야 함
    # --> {user_id: set()}
    # user별로 신고당한 횟수가 k번 이상인 경우 정지
    # --> len(set())
    
    mail_info = {}
    for user in id_list :
        mail_info[user] = 0
    # 메일을 몇개 받아야하는지 알아야 함
    # --> { user_id : 0}
   
    for report_detail in report :
        신고한, 신고당한 = report_detail.split(' ')
        report_info[신고당한].add(신고한)
        
    # 신고내역을 하나씩 확인하면서 
    # 신고당한사람: 신고한 사람들 목록을 채워준다.
    
    # report_info를 보고 유저별로 몇명이 신고했는지 k와 비교
    # (신고당한사람 : set('frodo', 'neo'))
    for key in report_info :
        if len(report_info[key]) >= k:
            for user in report_info[key]:
                mail_info[user] += 1
        
    # 정지 당했으면 >= k, 신고한 유저들 + 1
    
    # mail_info를 가지고 id_list 순서대로 값을 가져온다.
    for user in id_list :
        answer.append(mail_info[user])
    
    # answer = [메일을 받는 횟수]
    
    return answer 


# def solution(id_list, report, k):
#     answer = []
#     log_list = []
#     su_dict = {}
#     ban_list = []
#     log_dict = {}
#     for rep in report :
#         # 신고 로그
#         su_user = rep.split(' ')[0]
#         ban_user = rep.split(' ')[1]
#         # log list 생성
#         log_list.append([su_user, ban_user])
#     # 신고 중복 제거
#     # log_list = set(log_list)
#     # dict 형태로 만들어주기
#     for log in log_list :
#         if log[0] not in log_dict :
#             log_dict[log[0]] = log[-1]
#         else :
#             log_li = log_dict[log[0]]
#             log_dict[log[0]] = log_li + ' ' + log[1]
#     # 로그딕트에 없으면 빈 []
#     for id1 in id_list :
#         if id1 not in log_dict:
#             log_dict[id1] = 'null'


#     # 전체 기준 신고 횟수 count
#     for id1 in id_list:
#         su_nm = 0
#         for log in log_dict:
#             if id1 in log_dict[log]:
#                 su_nm += 1
#         su_dict[id1] = su_nm
#     # 신고당한 내역이 없는 경우
#     if id1 not in su_dict:
#         su_dict[id1]  = 0
#     # 밴 리스트에 추가
#     for ba in su_dict :
#         if su_dict[ba] >= k:
#             ban_list.append(ba)
#     # 메일 발송 횟수
#     for us in id_list:
#         mail_nm = 0
#         for lo in log_dict[us].split(' '):
#             try :
#                 if lo in ban_list:
#                     mail_nm += 1
#             except :
#                 pass
#         answer.append(mail_nm)


#     return answer

'''
값은 나오는데
채점 점수가.....................
눈물이 납니다
'''