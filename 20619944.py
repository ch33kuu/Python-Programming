import smtplib
uid='bhavya.exackt@gmail.com'
pwd='BHAVYA123'
to='bhavyajain1721@gmail.com'
sub='henlo'
body='henlo my fren'
mail=smtplib.SMTP('smtplib.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(uid,pwd)
msg="\r\n".join(['To:%s'%(to),'From :%s'%(uid),'Subject:%s'%(sub),body])
mail.sendmail(uid,[to],msg)
