import os
import sys

if not os.getegid() == 0:
    print("""\033[1;33m[!]Run installer as root!\033[1;m""")
    sys.exit()

def main():
    print("""\033[1;34m\n
#####################################################
##################[CLEANX INSTALLER]#################
#####################################################

---- Do you want to install cleanx on your computer?[Y/n]: 
    """)
    ans = raw_input("""\033[1;32m[*]=> \033[1;m""")
    if ans == 'y':
        os.popen("mkdir -p /opt/cleanx && touch  /opt/cleanx/log.txt && touch  /opt/cleanx/def_log.txt")
        print("""\033[1;32m[+]Succesfully installed cleanx. Use sudo python cleanx.py -c to begin\033[1;m""")
    else:
        sys.exit("""\033[1;32m[*]Close installer, buy!\033[1;m""")