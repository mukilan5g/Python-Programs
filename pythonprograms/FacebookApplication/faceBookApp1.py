import time

userName=[]
userFirstname=[]
userLastName=[]
userMailId=[]
userPassWord=[]
userMobno=[]

userNameFile=open("fnamefile.txt", "r")
userFirstnameFile=open("fFirstnamefile.txt", "r")
userLastNameFile=open("fLastnamefile.txt", "r")
userMailIdFile=open("fmailfile.txt", "r")
userPassWordFile=open("fpassfile.txt", "r")
userMobnoFile=open("fmobfile.txt", "r")

for line in userNameFile:
    userName.append(line[:-1])

for line in userFirstname:
    userFirstname.append(line[:-1])

for line in userLastName:
    userLastName.append(line[:-1])

for line in userMailId:
     userMailId.append(line[:-1])

for line in userPassWord:
    userPassWord.append(line[:-1])

for line in userMobno:
    userMobno.append(line[:-1])       

def signUp():
    num=["1234567890"]                        #num=[0,1,2,3,4,5,6,7,8,9]
    alpha=["abcdefghijklmnopqrstuvwxyz"]      #alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    splchar=['~','!','@','#','$','%','^','&','*','(',')','_','+','|','}','{','"',':','?','>','<','`','-','=','[',']','.','/']
    capAlpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mail=""
    psw=""
    uname=""
    fname=""
    lname=""
    mno=""

    uname=raw_input("Enter username:")
    userName.append(uname)
    filewrite(userName)

    fname=raw_input("Enter firstname:")
    userFirstname.append(fname)
    filewrite(userFirstname)

    lname=raw_input("Enter lastname:")
    userLastName.append(lname)
    filewrite(userLastName)

    mno=int(raw_input("Enter mobname:"))
    if mno <= 11:
        userMobno.append(mno)
        filewrite(userMobno)
    
    
    while mail not in userMailId and len(mail)<8:
        mail=raw_input("Enter valid mail id")
        if mail not in userMailId:
            userMailId.append(mail)
            filewrite(userMailId)
            break
        print "Sorry, the entered mail id is already in ues"
        print "please entered valid mail id"
        ans=raw_input("Are you already in fb account with the same mail id ? (y/n)\n")

        if ans.lower()=='y':
            logIn()
        else:
            signUp()
             
    while len(psw)<8:
        psw=raw_input("Please assign valid password and must have atleat 8 charecters\n")
       
        if len(psw)>8:
            if psw in num and psw in alpha and psw in splChar and psw in capAlpha:
                password=psw
                userPassWord.append(psw)
                filewrite(userPassWord)
                break
            else:
                print "Entered password not valid"
    return uname,fname,lname,mno,mail,psw

def filewrite(item):
    if item==userName:
        text=open("fnamefile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()

    if item==userFirstname:
        text=open("fFirstnamefile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()
    if item==userLastName:
        text=open("fLastnamefile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()
    if item==userMobno:
        text=open("fmobfile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()
    if item==userMailId:
        text=open("fmailfile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()
    if item==userPassWord:
        text=open("fpassfile.txt",'w')
        for i in item:
            text.write(i+"\n")
        text.close()    

def logIn():
    mail=""
    psw=""
    mail=raw_input("Enter mail id")
    txt=open("fmailfile.txt", "r")
    text=txt.read()
    if mail in text:
        psw=raw_input("Enter password")
        txt1=open("fpassfile.txt", "r")
        text1=txt1.read()
        if psw in text1:
            submit()
            print "Successfully logged in"
        else:
            print "password is not valid please enter correct mailid or password"
            logIn()
        
             
def submit():
    print("logging"),
    time.sleep(1)
    print ("..")
    time.sleep(1)
    print("..")
    time.sleep(1)  
