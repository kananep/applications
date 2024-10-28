from email.mime.text import MIMEText
import smtplib
import ssl

def send_email(email,height,average_height ,count):
    from_email = 'projectw161@gmail.com'
    from_password = 'yjkn dpby qgku pyiz'
    to_email = email
    
    subject = 'Height data'
    message = 'Hey there, your height is <strong>%s</strong>. <br> And the Average height of all height is <strong>%s</strong> ,calculated out of <strong>%s</strong> users. <br> Thank you' % (height, average_height, count)


    msg = MIMEText(message , 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    
    
    
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
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
    
    