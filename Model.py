#!/usr/bin/env python
# Written by: DGC

import smtplib

#==============================================================================
class Email:
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    def __init__(self):
        # initialise the variables to blank strings
        self.server = ""
        self.email = ""
        self.recipient = ""
        self.username = ""
        self.password = ""
        self._error = "Non-specified error"
        self.authenticate = False
 
    def send(self, message):
        """
        Sends the message to the defined email address from the given sender 
        using the server.
        If it doesn't have enough information to send it will return False 
        and register an error, otherwise True is returned.
        """
        # mainly for debugging purposes but it's nice to see what you're writing
        # and to whom
        print("Message \"%s\"" %(message))
        print("From: %s" %(self.email))
        print("To: %s" %(self.recipient))
        print("Using server: %s" %(self.server))
        
        # only print username/password if it authenticates and then replace 
        # password charactures with *
        if (self.authenticate):
            print("Username: %s" %(self.username))
            # don't print a password
            printable_password = ""
            for s in self.password:
                printable_password += "*"
            print("Password: %s" %(printable_password))
        print("")
        # if there is sufficent information then try to connect with the server
        if (self.valid()):
            try:
                server = smtplib.SMTP(self.server)
            except smtplib.socket.gaierror:
                self._error = "SMTP error on server: " + self.server
                return False
            else:
                # if the server is connected with then proceed
                if (self.authenticate):
                    server.login(self.username, self.password)
                server.sendmail(self.email, self.recipient, message)
                server.quit()
                return True
        else:
            return False

    def valid(self):
        """
        Checks if there is enough information to send an email, only checks 
        that the values are non-empty. There are  no sanity checks such as
        looking for '@' signs in emails or servers strings.
        """
        
        # only bother with username/password if we need to authenticate
        if (self.authenticate):
            if (self.username == "" or self.password == ""):
                self._error = "No Authentification details"
                return False

        if (self.server == ""):
            self._error = "No server"
            return False

        if (self.email == ""):
            self._error = "No senders email address"
            return False

        if (self.recipient == ""):
            self._error = "No recieving email address"
            return False
        # nothing checked is wrong, if an error is needed something unexpected 
        # has happened
        self._error = "Non-specified error"
        return True

    def error(self):
        """Returns what is wrong with the email information"""
        return self._error

#==============================================================================
if (__name__ == "__main__"):
    #
    # History
    # When     What
    # -------- ----------------------------------------------------------------
    # 29/05/12 Written.
    #--------------------------------------------------------------------------

    # a small test to check the model still works
    sender = Email()
    sender.valid()
    assert(sender.error() == "No server")

    sender.server = "pat.delcam.com"
    sender.valid()
    assert(sender.error() == "No senders email address")

    sender.email = "dgc@delcam.com"
    sender.valid()
    assert(sender.error() == "No recieving email address")

    sender.recipient = "davidcorne@gmail.com"
    sender.valid()
    assert(sender.error() == "Non-specified error")

    sender.authenticate = True
    sender.valid()
    assert(sender.error() == "No Authentification details")

    sender.username = "David"
    sender.valid()
    assert(sender.error() == "No Authentification details")

    sender.password = "password"
    sender.valid()
    assert(sender.error() == "Non-specified error")

    print("All tests passed, now trying to send via delcam server")
    print("")
    
    # don't need authentification
    sender.authenticate = False
    # will send an email if it connects
    sender.send("model.py test email")
    
