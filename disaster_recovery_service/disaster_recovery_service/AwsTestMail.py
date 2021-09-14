import smtplib
s = smtplib.SMTP('email-smtp.us-east-2.amazonaws.com')

s.connect('email-smtp.us-east-2.amazonaws.com',587)
s.starttls()

msg = 'From:hollygracemaguire@gmail.com\nTo: hollygracemaguire@gmail.com\nSubject: test email\n\n Change detected'

s.login('AKIAZA7BBNY6OX2EG6DO','BD+XSXbrtil9ssB9+8gfsUUmbsQpEwx757KID6s3eqke')
s.sendmail('hollygracemaguire@gmail.com','hollygracemaguire@gmail.com',msg)


