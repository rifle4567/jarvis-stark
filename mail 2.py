import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kishoreprabhu768@gmail.com", "kishoreprabhu@18")
 
msg = "hello!"
server.sendmail("kishoreprabhu768@gmail.com", "abeykakkuzhi@gmail.com", msg)
server.quit()
