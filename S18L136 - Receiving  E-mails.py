
# To read and search recieved emails we will use the built-in "imaplib" Library.
# We will also use the built-in "email" library for parsing through the recieved emails.
# The "imaplib" Library has a special syntax for searhing your Inbox.

import imaplib

# Make a connection to a IMAP Server. Depending on Domain Provider.
M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")

M.login(email, password)
# ('OK', [b'...@gmail.com authenticated (Success)'])

# To see List of available Email Categories:
M.list()

M.select('inbox')
# ('OK', [b'38'])


# Tuple unpacking:
typ, data = M.search(None, 'SUBJECT "NEW TEST PYTHON"') # No space "'

print(typ)
# OK

email_id = data[0]

result, email_data = M.fetch(email_id, '(RFC822)')     #'(PROTOCOL)'

# Should be too much info:
print(email_data)
# lots of Personal info + Email letter content


# Grab necessary:
raw_email = email_data [0][1] #may be different numbs


#Decode is important for better output result:
raw_email_string = raw_email.decode('utf-8')


#Using buid-in "email" Library to Parse that string:
import email


email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():

    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)

        print(body)
        # b'hello this is a test\r\n'


# 'text/plain'  >>> when you arу expecting a plain text
# 'text/html'   >>> when someone provided a Link in the Email.

