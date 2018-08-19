import imaplib

import mailparser

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('johnmcloy77@gmail.com', 'johnmcloy@123')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = data[0][1] # here's the body, which is raw text of the whole email

#email_message = mail.message_from_string(raw_email)
 
#print email_message['To']
 
#print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
 
#print email_message.items() # print all headers

mail5 = mailparser.parse_from_bytes(raw_email)

x =str(mail5.body.split("--- mail_boundary ---")[0])
print(x)
#print(mail5.text_plain)
for name in mail5.from_:
	print ("Name is ",name[0]," MailID is ",name[1]," SUbject is ")

print(mail5.subject)
