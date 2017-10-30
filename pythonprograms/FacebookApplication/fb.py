userName=[]
userFirstname=[]
userLastName=[]
userMailId=[]
userPassWord=[]
userMobno=[]

userNameFile=open("fnamefile.txt", "r")
userFirstname=open("fFirstnamefile.txt", "r")
userLastName=open("fLastnamefile.txt", "r")
userMailId=open("fmailfile.txt", "r")
userPassWord=open("fpassfile.txt", "r")
userMobno=open("fmobfile.txt", "r")

def signUp():
    
    num=["1234567890"]                        #num=[0,1,2,3,4,5,6,7,8,9]
    alpha=["abcdefghijklmnopqrstuvwxyz"]      #alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #splChar=['~','!','@','#','$','%','^','&','*','(',')','_','+','|','}','{',':','"','?','>','<','`',',','.','/',''',';','[',']','=','-','\']
    splChar=["~!@#$%^&*()_+|}{:"?><`-=[]\;',./"]
    capAlpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mail=""
    psw=""

    while mail not in userMailId and len(mail)<8:
             mail=raw_input("Enter valid mail id")
             if mail in num AND mail in alpha AND mail in splchar:
                     if mail.lower() not in userMailId:
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
                             userPassWord=append(psw)
                             username=raw_input("Enter username:")
                             userName=username
                             userNameFile.append(userName) 
                             firstname=raw_input("Enter firstname:")
                             userFirstname=firstname
                             userFirstname.append(userFirstname)
                             lastname=raw_input("Enter lastname:")
                             userLastName=lastname
                             userLastName.append(userLastName)
                             mobno=raw_input("Enter mobname:")
                             userMobno=mobno
                             userMobno.append(userMobno)
                     print "Entered password not valid"
     return username,firstname,lastname,mobno,mail,psw                
def filewrite(item):
             if item==userMailId:
                     text=open("fnamefile.txt",'w')
                     for i in item:
                             text.write(i+"\n")
                     text.close()

def logIn():
             mail=""
             psw=""
             while mail not in userMailId:
                     mail=raw_input("Enter mailId:")
                     if mail in userMailId:
                             psw=raw_input("Enter password")
                             if psw in userPassWord:
                                     self.submit()
                                     print "Successfully logged in"
                             else:
                                     print "Entered password is not valid"
                                     logIn()
             
             
 
def submit(self):
            print("logging"),
            time.sleep(1)
            print ("..")
            time.sleep(1)
            print("..")
            time.sleep(1)            
             
             
             

             
