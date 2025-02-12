import smtplib
my_email = "abc@gmail.com" # put your email
to_email = "def@gmail.com" # put your another email
password = "xxxzzz" # use the app password option from your email
connection = smtplib.SMTP("smtp.gmail.com") #creating an object with email provider
connection.starttls() #using tls
connection.login(my_email,password) #login with your email and password from app
connection.sendmail(from_addr=my_email,
                    to_addrs=to_email,
                    msg="Subject:Hello Testing\n\nHello Dude! Are you ok?")
connection.close() # close the connection

'''
with  smtplib.SMTP("smtp.gmail.com") as connection: #creating an object with email provider
    connection.starttls() #using tls
    connection.login(my_email,password) #login with your email and password from app
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject:Hello Testing\n\nHello Dude! Are you ok?")


'''