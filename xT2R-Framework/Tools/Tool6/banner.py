import sys
import random
import time

def logo():
 clear = "\x1b[0m"
 colors = [36, 32, 34, 35, 31, 37]
 x = """ 

  $$$$$$\  $$\      $$\  $$$$$$\  $$$$$$$$\  $$$$$$\  $$\   $$\        $$$$$$\  $$\                           $$\                           
$$  __$$\ $$$\    $$$ |$$  __$$\ \____$$  |$$  __$$\ $$$\  $$ |      $$  __$$\ $$ |                          $$ |                          
$$ /  $$ |$$$$\  $$$$ |$$ /  $$ |    $$  / $$ /  $$ |$$$$\ $$ |      $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$$$$$$$ |$$\$$\$$ $$ |$$$$$$$$ |   $$  /  $$ |  $$ |$$ $$\$$ |      $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$  __$$ |$$ \$$$  $$ |$$  __$$ |  $$  /   $$ |  $$ |$$ \$$$$ |      $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |\$  /$$ |$$ |  $$ | $$  /    $$ |  $$ |$$ |\$$$ |      $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
$$ |  $$ |$$ | \_/ $$ |$$ |  $$ |$$$$$$$$\  $$$$$$  |$$ | \$$ |      \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\__|  \__|\__|     \__|\__|  \__|\________| \______/ \__|  \__|       \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                                                           
                                                                                                                                           
                                                                                                                                            
                                                                          
 Amazon Valid Email Checker    |  Code by MR 3BR00T                                  
 
 [+] instagram : @3BR00T


 [+] 1. Run Amazon Valid Email Checker 
 [+] 2. About me [ for any help ! ]

+-------- With Great Power Comes Great Responsibilities! --------+

			                  """
 for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )