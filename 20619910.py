import smtplib
import imaplib
mail= imaplib.IMAP4_SSL('smtp.gmail.com')
mail.login('bhavya.exackt@gmail.com','BHAVYA123')
mail.select('inbox')
_,data = mail.search(None,'All')
kid=data[0].split()[-1]
_,content=mail.fetch(kid,'(RFC822)')
