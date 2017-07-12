import sys
import smtplib
import os

if not 'MINER_NOTIFY_EMAIL' in os.environ:
	print('  You should set environment variable MINER_NOTIFY_EMAIL')
	sys.exit(0)

hostname = os.environ['COMPUTERNAME']
email = os.environ['MINER_NOTIFY_EMAIL']


from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def sendemail(from_addr, to_addr_list, cc_addr_list,
			subject, message,
			login, password,
			smtpserver='smtp.gmail.com:587'):
	header  = 'From: %s\n' % from_addr
	header += 'To: %s\n' % ','.join(to_addr_list)
	header += 'Cc: %s\n' % ','.join(cc_addr_list)
	header += 'Subject: %s\n\n' % subject
	message = header + message

	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(from_addr, to_addr_list, message)
	server.quit()
	return problems

text = 'Your computer ' + hostname + ' is started: '
plus = text + str(now)

args = sys.argv[:3]

if len(args) < 3:
	print('  You should set subject/message argument. ' + '\n' '  Example: program.exe \"Here subject\" \"Here message\"')
	exit()

sendemail(from_addr = 'service@gmail.com', 
to_addr_list = [email], 
cc_addr_list = [''], 
subject = sys.argv[1],
message = sys.argv[2],
login = 'service@gmail.com',
password = '***********')

print('The message was sent to ' + email)