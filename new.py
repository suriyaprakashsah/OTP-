import random
import time
import smtplib
import pymysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
db = pymysql.connect("46.4.115.158", "root", "Mysql@rhombus123", "demo")
x = db.cursor()
name = raw_input("Enter the name: ")
#print(name)
email = raw_input("Enter the email ID: ")
#print(email)
mobile = raw_input("Enter mobile No: ")
#print(mobile)
OTP = random.randint(1,10000)
otp1=str(OTP)
#print(OTP)
time = localtime = time.asctime( time.localtime(time.time()))
a = localtime.split()
b = a[3]
print(b)
x.execute("""INSERT INTO uber VALUES (%s,%s,%s,%s)""", (name,mobile,b,OTP))
print("Successfully Inserted")


# me == my email address
# you == recipient's email address
x.execute("SELECT  OTP, name from uber")

# fetch all of the rows from the query
data = x.fetchall ()

# print the rows
for row in data :
 print row[0], row[1]
db.commit()
db.close()

me = "aishuyadav2233@gmail.com"
you = "snikhilsingh85@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "OTP"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the your OTP:\n" + otp1

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText('plain'+ text)

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
# Send the message via local SMTP server.  7
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('Enter email', 'Enter password')
mail.sendmail(me, you, msg.as_string())
mail.quit()
x.execute("SELECT * FROM verification where otp = %s", otp1)
verification = x.fetchall()
print(verification)
