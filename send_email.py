from email.mime.text import MIMEText
import smtplib
import ssl


# def send_email(email):
#     from_email = 'projectw161@gmail.com'
#     from_password = 'wbsz nqwh ezxu xxxv'  # Make sure this is your Gmail App Password
#     to_email = email

#     subject = 'Email Marketing'
#     message = '<h1>Welcome!</h1><p>This is a marketing email.</p>'

#     msg = MIMEText(message, 'html')
#     msg['Subject'] = subject
#     msg['To'] = to_email
#     msg['From'] = from_email

#     gmail = None
#     try:
#         gmail = smtplib.SMTP('smtp.gmail.com', 587)
#         gmail.set_debuglevel(1)  # Optional: shows more logs
#         gmail.ehlo()
#         gmail.starttls()
#         gmail.login(from_email, from_password)
#         gmail.send_message(msg)
#         print("Email sent successfully!")
#     except Exception as e:
#         print("Error sending email:", str(e))
#     finally:
#         if gmail:
#             gmail.quit()



def send_email():
    from_email = 'projectw161@gmail.com'
    from_password = 'wbsz nqwh ezxu xxxv'
    to_email = 'projectw161@gmail.com'
    
    subject = 'Email Marketing'
    message = '<h1>Welcome!</h1><p>This is a marketing email.</p>' 


    msg = MIMEText(message , 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    
    
    
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.set_debuglevel(1)
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        gmail.quit()







    
    # context = ssl.create_default_context()
    
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
    #     smtp.login(from_email , from_password)
    #     smtp.sendmail(from_email,to_email , msg)
        
        
        
    
    # gmail = smtplib.SMTP('smtp.gmail.com' , 587)    
    # gmail.ehlo()
    # gmail.starttls()
    # gmail.login(from_email,from_password)
    # gmail.send_message(msg)
    
    