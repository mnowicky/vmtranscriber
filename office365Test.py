#POP3LIB test script, connects to voicemail@outlook.com, lists messages and prints them.

import poplib
import email
import re
pop3server = 'outlook.office365.com'
username = 'voicemail@williammattar.com'
password = 'Matt@r2019!'
pop3server = poplib.POP3_SSL(pop3server)
print (pop3server.getwelcome())
pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat()
mailcount = pop3info[0]
print('Total no. of email: ' + str(mailcount))
print('\n\nStart Reading Messages\n\n')

def procMessage(messageNum):
	raw_message = pop3server.retr(messageNum)[1]
	str_message = email.message_from_bytes(b'\n'.join(raw_message))
	body = str(str_message.get_payload()[0])
	#print(body)
	messageUID=str(pop3server.uidl(messageNum))
	messageUID=re.findall(r'\d+',messageUID,0)[1]
	#messageUID=messageUID.group(2)
	print(messageUID)
	


for msgNum in range(mailcount):
	try:
		procMessage(msgNum+1)
	except Exception as e:
		print(e)
		continue
