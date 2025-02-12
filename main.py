import random, datetime as dt, smtplib, pandas
my_email = "mnop@gmail.com"
to_email = "kap@gmail.com"
password = "pass" # the password from using app password option in email



birthday = dt.datetime.now()
bd_tuple = (birthday.month,birthday.day)


data = pandas.read_csv("birthdays.csv")
bd_dict = {(row.month,row.day):row for (index, row) in data.iterrows()}
#print(bd_dict)
person_data = bd_dict[bd_tuple] # series data type from pandas
name = person_data["name"]
print(name)



file_path = rf"letter_{random.randint(1,3)}.txt"

if bd_tuple in bd_dict: # if the current weekday is wednesday
    with open(file_path,'r') as bd_wish:
        bd_lines = bd_wish.read()
        wish = bd_lines.replace("[NAME]", name) # name from person_data
        with  smtplib.SMTP("smtp.gmail.com") as connection: #creating an object with email provider
            connection.starttls() #using tls
            connection.login(my_email,password) #login with your email and password from app
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject: BirthdayWish\n\n{wish}")