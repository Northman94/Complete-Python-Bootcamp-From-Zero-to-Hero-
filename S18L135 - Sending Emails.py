# To send emails with Python, we need to manually go through the steps of:

# connecting to an Email Server;
# confirming connection;
# setting a protocol;
# logging on;
# and sending the message.


# Build-in Python "smtplib" Library, makes these steps simple function calls.
# Each major E-mail provider has their own  SMTP (Simple Mail Transfer Protocol) Server.


# Create an SMTP object for a server.

# Gmail(will need App Password) //  smtp.gmail.com
# Yahoo Mail // smtp.mail.yahoo.com
# Outlook.com / Hotmail.com // smtp - mail.outlook.com
# AT & T //  smpt.mail.att.net(Use port 465)
# Verizon // smtp.verizon.net(Use port 465)
# Comcast // smtp.comcast.net


import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587) #465 or no at All

# Greet server & establish the Connection:
# This method should be placed right after "smtp_object" creation.

smtp_object.ehlo() #Will get my Wi-Fi Router WAN IP

# Port: 587 = TLS Encription

# When using the 587 port, this means you are using TLS encryption,
# which you need to initiate by running the starttls() command.

# If you are using port 465, this means you are using SSL and you can skip this step.

# In order to initiate Encryption:

smtp_object.starttls()
# (220, b'2.0.0 Ready to start TLS')


# Never save RAW E-mail / Password in a Script!!!
# If you want your creds to be invisible while typing in => Getpass Library [Build-in Python].

password = input('What is your Password: ')
# What is your Password: 123


import getpass

password = getpass.getpass('Password please: ')
# Password please: ········



# Generate an App Password for G-mail user:

# Note for Gmail Users, you need to generate an app password instead of your normal
# email password. This also requires enabling 2-step authentication.

# https://support.google.com/accounts/answer/185833?hl=en/

# Set-up 2 Factor Authentication, then create the App Password,
# choose Mail as the App and give it any name you want.
# This will output a 16 letter password for you.
# Pass in this password as your login password for the smtp.
# Google Account > Security > Signing-in to Google > App Pasword > Mail > Device: Custom Name


email = getpass.getpass("Enter your email: ")

password = getpass.getpass("Enter your password: ")

smtp_object.login(email,password)
# Enter your email: ········
# Enter your password: ········
# (235, b'2.7.0 Accepted')


# Send E-mail right after Login.
# Otherwise you may be disconnected.
# And will need to generate Password again


from_address = email

to_address = email #to my self

subject = input("Enter the Subject Line: ")
message = input("Enter the Body message: ")

# Better not change this format:
msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)
# Enter the Subject Line: NEW TEST PYTHON
# Enter the Body message: hello this is a test
# Out[24]:
# {}

# '{}'  output in Jupiter means - successful sending
# Otherwise it's Error in credentials OR Connection Loss


# Quit & Close session:
smtp_object.quit()
# (221,
#  b'2.0.0 closing connection z3-20020adfdf83000000b00212a83b93f3sm2878864wrl.88 - gsmtp')



