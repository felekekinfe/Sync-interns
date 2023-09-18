import random
import smtplib
from email.mime.text import MIMEText

sender=input('sender email')
password=int(input('your mail password as integer'))
reciever=input('reciever email')
message=input('your message')


def generate_otp():
    global otp_code
    otp_code=''
    
    rand_value=random.sample(range(0,9),6)
    for i in rand_value:
        otp_code+=str(i)
    return int(otp_code)

def send_mail(sender,password,receiver,message):
    generate_otp()
    print(otp_code)
    port = 1025
    msg = MIMEText(message)

    msg['Subject'] = 'Test mail'
    msg['From'] = sender
    msg['To'] = receiver



    try:
        connect=smtplib.SMTP('smtp.gmail.com',port=port)
        connect.starttls()
        connect.login(sender,password=password)
        connect.sendmail(sender, receiver,msg.as_string())

        your_otp=int(input('Verify your email by entering your OTP'))
        while True:
            if your_otp==otp_code:
                print('Your Verified!')
                break
            else:
                print("incorrect OTP,try again!!")
                your_otp=int(input())
    except:
        print('cant be sent!!')
       
send_mail(sender,password,reciever,message)


