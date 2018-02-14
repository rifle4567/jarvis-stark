#email program

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("kishoreprabhu768@gmail.com","kishoreprabhu@18")

msg = "hello world"
server.sendmail("kishoreprabhu768@gmail.com","imnotkoushik007@gmail.com",msg)
print ("message sent succesfull")
server.quit()
