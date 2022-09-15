from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
import smtplib 

def send_email(from_user, to_users, user_password, contents, SMTP_SERVER = 'smtp.naver.com',SMTP_PORT = 465, title='제목',attachments=[], cc_targets=[]):
    '''
    이메일을 발송하는 함수입니다.

    ** 필수값 **
    from_user : 메일 보내는 아이디
    to_users : 메일 받는 아이디
    user_password : 메일 보내는 아이디 비번
    contents : 메일 내용
    
    '''

    try:
        TO_USER = ','.join(to_users)
    except:
        print('메일 받는 대상들의 리스트를 확인하세요')


    # 편지봉투 만들기
    msg = MIMEMultipart('alternative')

    # 첨부파일여부
    if attachments :
        try :
            msg = MIMEMultipart('mixed')
            email_file= MIMEBase('application', 'octet-stream')
            # 바이너리 리드
            for attachment in attachments :
                with open(attachment, 'rb') as f:
                    file_data= f.read()
                email_file.set_payload(file_data)
                encoders.encode_base64(email_file)
                file_name= basename(attachment)
                email_file.add_header('Content-Disposition', 'attachment', filename=file_name,)
                msg.attach(email_file)
            print('첨부파일 완료')
        except :
            print('파일 경로를 확인하세요')

    # 참조 여부 확인
    if cc_targets :
        try:
            cc_target_str = ','+ ','.join(cc_targets)
        except:
            print('참조 리스트에 문제가 있습니다')
    else :
        cc_target_str = ''
        
    try : 
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
        print('메일 전송 서버 접속 성공')
        smtp.login(from_user, user_password)
        print('로그인 성공!')
        # msg에 값으로 넣어줌
        msg['From'] = from_user
        msg['To'] = TO_USER
        msg['Subject'] = title
        text = MIMEText(contents)
        msg.attach(text)
        smtp.sendmail(from_user, TO_USER + cc_target_str, msg.as_string())
        print('이메일 발송 성공!')
    except Exception as e :
        print('#### 에러 발생 ####')
        print(e)
        #에러 났을때
        pass
    finally:
        # 에러여부 상관없이 반드시 실행
        smtp.close()   

        