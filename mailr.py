import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from random import random
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
print("+++++++++++++++++++++++++++++++ WELCOME TO Mailr +++++++++++++++++++++++++++++++")
print("                                 Version 1.0.2            \n")
master_check=False
while(master_check==False):
    fw=open("data/email_data_loc.txt","r+")
    if(fw.readline()==""):
        loc=input("Enter the file location of your API client data (this file location will be stored for future useage)\n")
        fw.write(loc)
        fw.close()
    else:
        checking=False
        while(checking==False):
            a=input("Would you like to change your API client data file location? (y/n)\n")
            if(a!="y" and a!="n"):
                print("please enter a valid response(y/n)\n")
                checking=False
            elif(a=="y"):
                checking=True
                loc=input("Enter the file location of your API client data (this file location will be stored for future useage)\n")
                fw=open("data/email_data_loc.txt","r+")
                fw.seek(0)
                fw.truncate()
                fw.write(loc)
                fw.close()
                master_check=True
            else:
                checking=True
                master_check=True
fw=open("data/email_data_loc.txt","r+")
creds = ServiceAccountCredentials.from_json_keyfile_name(fw.readline(), scope) # /Users/shivamsyal/Downloads/client_data.json
client = gspread.authorize(creds)
sheet_name="SPREADSHEET_NAME_HERE"
sheet = client.open(sheet_name).sheet1
val=5 # CHANGE THIS VALUE TO THE COLUMN YOU WANT TO USE!!
email_send = sheet.col_values(val)
x=len(email_send)
test=False
while(test==False):
    ans=input("Do you have a range of emails you want to use? (\'y\' = you have a range, \'n\' = you want to use all emails)\n")
    if(ans=="y"):
        test=True
        r_start=int(input("Enter the FIRST value of the range (\'1\' is minimum)\n"))
        r_end=int(input("Enter the LAST value of the range (\'"+str(x)+"\' is maximum)\n"))
        temp1=False
        temp2=False
        while(temp1==False and temp2==False):
            if(r_start<1 or r_start>r_end or r_start>x):
                r_start=int(input("Please enter a valid FIRST value for your range (\'1\' is minimum)\n"))
            else:
                temp1=True
            if(r_end>x or r_end<r_start or r_end<1):
                r_end=int(input("Please enter a valid LAST value for your range (\'"+x+"\' is maximum)\n"))
            else:
                temp2=True
        for y in range(0,r_start-1):
            email_send[y]=''
        for i in range(r_end,x):
            email_send[i]=''
    elif(ans=="n"):
        test=True
    else:
        test=False
        print("Please enter a valid answer (y/n)\n")
email_send[0]=''
print("\nRetrieving all VALID emails...")
r=random()*5
time.sleep(r)
print("Processing...")
r=random()*5
time.sleep(r)
print("Successfully collected emails from \'"+sheet_name+"\'\n")
r=random()*2
time.sleep(r)
for val in range(0,x):
    check=['@','.com','.org','.net']
    val1=email_send[val].find(check[0])
    val2=email_send[val].find(check[1])
    val3=email_send[val].find(check[2])
    val4=email_send[val].find(check[3])
    if(val1==-1 or (val2==-1 and val3==-1 and val4==-1)):
        email_send[val]= ''
checking=False
while(checking==False):
    p_ans=input("Would you like to print the emails selected? (y/n)\n")
    if(p_ans!="y" and p_ans!="n"):
        print("Please enter a valid response (y/n)\n")
    elif(p_ans=="y"):
        
        print("Printing...")
        r=random()
        time.sleep(r)
        checking=True
        if(ans=="y"):
            print("\n")
            for x in range(r_start-1,r_end):
                if(email_send[x]!=''):
                    print(email_send[x])
        else:
            print("\n")
            for x in range(0,x):
                if(email_send[x]!=''):
                    print(email_send[x])
    else:
        break
check=False
while(check==False):
    
    s_ans=input("\nAre you sure you would like to send your message? (y/n)\n")
    if(s_ans!="y" and s_ans!="n"):
        print("Please enter a valid answer (y/n)\n")
    elif(s_ans=="y"):
        check=True
        email_user = 'SENDER_EMAIL_HERE'
        email_password = 'SENDER_PASSWORD_HERE'
        subject = 'EMAIL_SUBJECT_HERE'
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = ", ".join(email_send)
        msg['Subject'] = subject
        stuff=open("data/email_message_text.txt","r+")
        body = stuff.read()
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        print("Sending...")
        r=random()*5
        time.sleep(r)
        server.sendmail(email_user,email_send,text)
        server.quit()
        print('Mail Sent')
        stuff.close()
    else:
        check=True
        break
print("\nTHANK YOU FOR USING Mailr!")
