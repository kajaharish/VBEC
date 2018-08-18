import mailparser
import email
import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('johnmcloy77@gmail.com', 'johnmcloy@123')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox")  # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0]  # data is a list.
id_list = ids.split()  # ids is a space separated string
i = 1
for x in reversed(range(-10,0)):

    latest_email_id = id_list[x]  # get the latest

    result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

    raw_email = data[0][1]  # here's the body, which is raw text of the whole email
    mail5 = mailparser.parse_from_bytes(raw_email)

    # print(mail5.body)
    for name in mail5.from_:
        print(i,". Name is " + name[0], ", MailID is " + name[1], ", Subject is ", end=" ")
        i += 1
    print(mail5.subject)


#email_message = email.message_from_string(raw_email)

# print email_message['To']

# print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>

# print email_message.items() # print all headers

