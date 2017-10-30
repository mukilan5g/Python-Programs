def toCreateFacebook(self):
    print "Welcome to facebook website page\n"
    promt=int(raw_input("""To ctreate new account press 1\n"""+
                            """To login press 2\n"""))
    if prompt==1:
        user=FbAcount()
    elif prompt==2:
        acc=loginAcc()
    else:
        print "The entered key is invalid,try agin"
        toCreateFacebook()
class FbAcount:
    def __init__(self):
        self.username,self.firstname,self.lastname,self.password,self.mobno,self.emailId=signUp()
        print "Thank you %s,your facebook account is created successfully and ready to use"%username
        time.sleep(2)
        
      
