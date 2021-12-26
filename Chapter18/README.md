```
1. What is the protocol for sending email? For checking and receiving email?
```
```
Answer:
> SMTP - Simple Mail Transfer Protocol - Sending email

> IMAP - Internet Message Access Protocol - Checking and Receiving email
```
-----------------------------------------------------
```
2. What four smtplib functions/methods must you call to log in to an SMTP server?
```
```
Answer:
> import smtplib

> smtpObj = smtplib.SMTP('smtp.example.com', 587)

> smtpObj.ehlo()

> smtpObj.starttls()
```
-----------------------------------------------------
```
3. What two imapclient functions/methods must you call to log in to an IMAP server?
```
```
Answer:
> import imapclient

> imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
```
-----------------------------------------------------
```
4. What kind of argument do you pass to imapObj.search()?
```
```
Answer:
> imapObj.search(['ALL'])

> imapObj.search(['ON date])

> imapObj.search(['SINCE date', 'BEFORE date', 'UNSEEN'])

> imapObj.search(['SINCE date', 'FROM email@example.com'])

> imapObj.search(['SINCE date', 'NOT FROM email1@example.com'])

> imapObj.search(['OR FROM email1@example.com FROM email2@example.com']).

> imapObj.search(['FROM email1@example.com', 'FROM email2@example.com']).
```
-----------------------------------------------------
```
5. What do you do if your code gets an error message that says got more than 10000 bytes?
```
```
Answer:
> You will have to disconnect and reconnect to the IMAP server and try again.
```
-----------------------------------------------------
```
6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?
```
```
Answer:
> pyzmail module
```
-----------------------------------------------------
```
7. When using the Gmail API, what are the credentials.json and token.json files?
```
```
Answer:
> credentials.json - Is where the Username and password is stored

> token.json - Is where the token for the Gmail API is stored (Unique API TOKEN)
```
-----------------------------------------------------
```
8. In the Gmail API, what’s the difference between “thread” and “message” objects?
```
```
Answer:
> Thread Object - To represent conversation threads of the mails

> Message Object - that holds a list of GmailMessage Objects
```
-----------------------------------------------------
```
9. Using ezgmail.search(), how can you find emails that have file attachments?
```
```
Answer:
> ezgmail.search('has:attachment')
```
-----------------------------------------------------
```
10. What three pieces of information do you need from Twilio before you can send text messages?
```
```
Answer:
> 1. Have to install twilio - pip install twilio

> 2. Have to sign up - https://twilio.com/

> 3. Verification code send to the phone number
```
-----------------------------------------------------
