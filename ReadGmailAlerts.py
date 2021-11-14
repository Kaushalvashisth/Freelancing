# Importing libraries
import imaplib, email
import re

#enter email and password here
user = 'enter your email here'
password = ''
imap_url = 'imap.gmail.com'

# Function to get email content part i.e its body part
def get_body(msg):
	if msg.is_multipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

# Function to search for a key value pair
def search(condition, mail):
	result, data = mail.search(None, condition)
	return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
	msgs = [] # all the email data are pushed inside an array
	for num in result_bytes[0].split():
		typ, data = mail.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

# remove links from body using regex
def remove_links(body):
    text = re.sub('<http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', body, flags=re.MULTILINE)
    text = re.sub('[<>]', '', text)
    return text

#extract stocks from string 
# returns stocks string
def extract_stocks(text):
    start=text.find("Below is the list of new stocks filtered through scan")+54
    end=text.find("View all triggers for this alert")
    
    stocks=text[start:end] 
    return stocks

def split_stocks(stocks):
   stocks=re.split('\n|\r',stocks)
   stocks=list(filter(None, stocks))
   return stocks

def write_to_file(stocks):
    fileName=""
    if stocks[0]!=None:
        fileName=stocks[0]
    
    f= open(fileName+".txt","w+")
    for i in stocks[1:]:
        if i!=' ' and i!='' and i!=None:
            f.write(i+"\n")
        
    print("Stocks are written in file ",fileName)
    f.close()

# this is done to make SSL connnection with GMAIL
mail = imaplib.IMAP4_SSL(imap_url)

# logging the user in
mail.login(user, password)

# calling function to check for email under this label
mail.select('Inbox')

# fetching emails from this user "user@gmail.com"
condition='(FROM "your_email@gmail.com" BODY "View all triggers for this alert")' # we can add UNSEEN for not seen messages 
msgs = get_emails(search(condition, mail))

print("Number of Emails = ",len(msgs),"\n")

#i=1
for msg in msgs:
    # extract body
    body=get_body(email.message_from_bytes(msg[0][1]))
    # convert to string
    body = str(body, 'utf-8')
    if body.find("Below is the list of new stocks filtered through scan")!=-1 and body.find("View all triggers for this alert")!=-1:
        
        # remove links
        new_body=remove_links(body)
        
        # extract stocks
        stocks=extract_stocks(new_body)
        
        print(stocks)
        
        #split stocks into array
        new_stocks=split_stocks(stocks)
        
        #write stocks to txt file
        write_to_file(new_stocks)
        print("\n\n")

# printing them by the order they are displayed in your gmail

#for msg in msgs[::-1]:
#	for sent in msg:
#		if type(sent) is tuple:
#
#			# encoding set as utf-8
#			content = str(sent[1], 'utf-8')
#			data = str(content)
#
#			# Handling errors related to unicodenecode
#			try:
#				indexstart = data.find("ltr")
#				data2 = data[indexstart + 5: len(data)]
#				indexend = data2.find("</div>")
#
#				# printtng the required content which we need
#				# to extract from our email i.e our body
#				print(data2[0: indexend],"\n\n")
#			except UnicodeEncodeError as e:
#				pass
