#-*- coding: utf-8 -*-
import os
import sys



#Variables for directories
def_log_directory = '/opt/cleanx/def_log.txt'
del_directory = '/opt/cleanx/delete.txt'  # type: str
log_directory = '/opt/cleanx/log.txt'

default_log_dir = ["/var/log/syslog",
                   "/var/log/messages",
                   "/var/log/auth.log",
                   "/var/log/secure",
                   "/var/log/dmesg",
                   "/var/log/alternatives.log",
                   "/var/log/anaconda.log",
                   "/var/log/audit",
                   "/var/log/boot.log",
                   "/var/log/cron",
                   "/var/log/cups",
                   "/var/log/faillog",
                   "/var/log/kern.log",
                   "/var/log/maillog",
                   "/var/log/mail.log",
                   "/var/log/pm-powersave.log",
                   "/var/log/spooler",
                   "/var/log/lastlog",
                   "/var/log/tallylog",
                   "/var/log/btmp",
                   "/var/log/utmp",
                   "/var/log/wtmp",
                   "/var/log/messages",
                   "/var/log/warn",
                   "/var/log/poplog",
                   "/var/log/qmail",
                   "/var/log/smtpd",
                   "/var/log/telnetd",
                   "/var/log/cups/access_log",
                   "/var/log/cups/error_log",
                   "/var/log/thttpd_log",
                   "/var/log/spooler",
                   "/var/spool/tmp",
                   "/var/spool/errors",
                   "/var/spool/locks",
                   "/var/log/nctfpd.errs",
                   "/var/log/acct",
                   "/var/apache/log",
                   "/var/apache/logs",
                   "/usr/local/apache/log",
                   "/usr/local/apache/logs",
                   "/usr/local/www/logs/thttpd_log",
                   "/var/log/news",
                   "/var/log/news/news",
                   "/var/log/news.all",
                   "/var/log/news/news.all",
                   "/var/log/news/news.crit",
                   "/var/log/news/news.err",
                   "/var/log/news/news.notice",
                   "/var/log/news/suck.err",
                   "/var/log/news/suck.notice",
                   "/var/log/xferlog",
                   "/var/log/proftpd/xferlog.legacy",
                   "/var/log/proftpd.xferlog",
                   "/var/log/proftpd.access_log",
                   "/var/log/httpd/error_log",
                   "/var/log/httpsd/ssl_log",
                   "/var/log/httpsd/ssl.access_log",
                   "/var/adm",
                   "/var/run/utmp",
                   "/etc/wtmp",
                   "/etc/utmp",
                   "/etc/mail/access",
                   "/var/log/mail/info.log",
                   "/var/log/mail/errors.log",
                   "/var/log/httpd/*_log",
                   "/var/log/ncftpd/misclog.txt",
                   "/var/account/pacct",
                   "/var/log/snort",
                   "/var/log/bandwidth",
                   "/var/log/explanations",
                   "/var/log/syslog",
                   "/var/log/user.log",
                   "/var/log/daemons/info.log",
                   "/var/log/daemons/warnings.log",
                   "/var/log/daemons/errors.log",
                   "/etc/httpd/logs/error_log",
                   "/etc/httpd/logs/*_log",
                   "/var/log/mysqld/mysqld.log"
                   "/root/.ksh_history",
                   "/root/.bash_history",
                   "/root/.sh_history",
                   "/root/.history",
                   "/root/*_history",
                   "/root/.login",
                   "/root/.logout",
                   "/root/.bash_logut",
                   "/root/.Xauthority"]


 # Checking if cleanx is running as root
if not os.geteuid() == 0:
    print("""\033[1;31m[!]You must run script as root""")
    sys.exit()


##Help function
def help():
    print("""\033[1;32m
    [ -c ] ------ Configuration mode (Add log file(s) path, configure delete.txt)
    [ -s ] ------ Soft mode (Remove content of files with /dev/null)
    [ -g ] ------ Grave mode (Delete files from computer)
    """)

################CONFIGURATION MOD FUNCTIONS######################################

def configure():
    if os.path.isfile(def_log_directory):
        file = open(def_log_directory, 'r')
        for line in file.readlines():
            line = line.rstrip('\n')
            r = 0
            for path in default_log_dir:
                if line == path:
                    r += 1
                else:
                    pass
            if r < 1:
                def_file = open(def_log_directory, 'a')
                def_file.write(path+'\n')
                def_file.close()


    else:
        for path in default_log_dir:
            if os.path.isfile(path):
                def_file = open(def_log_directory, 'a')
                def_file.write(path+'\n')
                def_file.close()
    print("""\033[1;37m\n
     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗██╗  ██╗
    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║╚██╗██╔╝
    ██║     ██║     █████╗  ███████║██╔██╗ ██║ ╚███╔╝ 
    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║ ██╔██╗ 
    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║██╔╝ ██╗
     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                      [Cleanx v1.0             ]
                      [Configuration mode      ]
                      [Author:varham           ]
                      [Mail: varhamov@gmail.com]
                                                     \033[1;m""")  # Banner
    menu()


def menu():  # Main menu function
    print("""\033[1;34m
########################################################
[*]Choose configure option:
[1] - Add log file
[2] - Configure delete.txt
[3] - Exit
#########################################################
     \033[1;m""")
    option = raw_input("""\033[1;32m[*]=> \033[1;m""")
    if option == "1":
        add_log()
    elif option == "2":
        conf()
    elif option == "3":
        sys.exit()


def add_log():  # Add log function
    print("""\033[1;37m[*]Enter log file directory (e.g. /home/user/folder/log).Type 'back' to return to main menu\033[1;m""")
    directory = raw_input("""\033[1;32m[*]=> \033[1;m""")
    if directory.lower() == 'back':
        menu()
    if os.path.isfile(directory):  # If file exist, adding it to log.txt
        log_file = open(log_directory, 'a')
        log_file.write(directory+'\n')
        log_file.close()
        print("""\033[1;32m[+]Succesfully added log file directory!\033[1;m""")
        menu()
    else:  # If file does not exits, call add_log again
        print("""\033[1;31m[-]Can't add log file path. Please check if directory is correct or if the file exist and try again\033[1;m""")
        add_log()


def conf(): #delete.txt configuration menu function
    if os.path.isfile(del_directory):
        print("""\033[1;34m\n
#########################################################
[*]Choose next configuration step:
[1] - Add new file directories to delete.txt
[2] - Remove file directories from delete.txt
[3] - Delete delete.txt
[4] - Return to main menu
#########################################################
        """)
        option = raw_input("""\033[1;32m[*]=> \033[1;m""")
        if option.lower == 'back' or option == "4":
            menu()
        elif option == "1":
            add()
        elif option == "2":
            remove()
        elif option == "3":
            os.popen("rm -f " + del_directory)
            print("""\033[1;32m[+]Successfully removed delete.txt!\033[1;m""")
            menu()
    else:
        print("""\033[1;33m[!]Delete.txt does not exist. Do you want to create one?[Y/n]\033[1;m""")
        ans = raw_input("""\033[1;32m=> \033[1;m""")
        if ans.lower() == 'y':
            add()
        elif ans.lower == 'n':
            menu()


def add(): #Add new logs to delete.txt function
    init_mas = create_init()
    print("""\033[1;37m[*]Choose log files you want to add to delete.txt(e.g. 1,2,4,6 or 1-8)\033[1;m""")
    i = 1
    for item in init_mas:#print all logs path from all files (def_log.txt, log.txt)
        print ('['+str(i)+'] ' + item)
        i+=1
    files = raw_input("""\033[1;32m[*]=> \033[1;m""")
    del_file = open(del_directory, 'a')
    if files == "back":
        conf()
    elif ',' in files:
        files = files.split(',')#split user input to get indexes of logs
        for num in files:
            located = check_path(num, init_mas)#check if the path exists in the file
            if located < 1: #if not, adding path to file
                del_file.write(init_mas[int(num)-1]+"\n")
        del_file.close()
        print("""\033[1;32m\n[+]Successfully added log file directories!\033[1;m""")
        conf()
    elif '-' in files:
        files = files.split('-')#split user input to get indexes of logs
        for num in range(int(files[0]), int(files[1])+1):
            located = check_path(num, init_mas)#check if the path exists in the file
            if located < 1:#if not, adding path to file
                del_file.write(init_mas[int(num)-1]+"\n")
        del_file.close()
        print("""\033[1;32m\n[+]Successfully added log file directories!\033[1;m""")
        conf()
    else:
        del_file.write(init_mas[int(files)-1])
        del_file.close()
        print("""\033[1;32m\n[+]Successfully added log file directories!\033[1;m""")
        conf()

def remove():  #Remove logs from delete.txt function
    del_buf = []
    del_file = open(del_directory, 'r')
    for line in del_file.readlines():
        line = line.rstrip('\n')
        del_buf.append(line)  #Reading all content from delete.txt and appending it ro def_buf[]
    del_file.close()
    print("""\033[1;37m[*]Choose log files you want to remove from delete.txt(e.g. 1,2,4,6 or 1-8)\033[1;m""")
    i = 1
    for path in del_buf:
        print('[' + str(i) + '] ' + path)  #Printing delete.txt content
        i += 1
    files = raw_input("""\033[1;37m[*]=> \033[1;m""")
    if files == 'back':
        conf()
    elif ',' in files:
        files = files.split(',')
        for num in files:
            del_buf[int(num)-1] = None #Removing content
        del_buf = filter(None, del_buf)
        print del_buf
        print("""\033[1;32m\n[+]Successfully remove log file directories!\033[1;m""")
        os.popen("rm -f " + del_directory)  #Removing delete.txt
        del_file = open(del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')  # Creating delete.txt and write remaining content to it
        del_file.close()
        conf()
    elif '-' in files:
        files = files.split('-')
        for num in range(int(files[0]), int(files[1])+1):
            del_buf[int(num)-1] = None #Removing content
        del_buf = filter(None, del_buf)
        print("""\033[1;32m\n[+]Successfully remove log file directories!\033[1;m""")
        os.popen("rm -f " + del_directory)#Removing delete.txt
        del_file = open(del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')  # Creating delete.txt and write remaining content to it
        del_file.close()
        conf()
    else:
        del del_buf[int(files)-1]
        os.popen("rm -f delete.txt")
        del_file = open(del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')
        del_file.close()
        print("""\033[1;32m\n[+]Successfully remove log file path!\033[1;m""")
        conf()


def check_path(num, init_mas):  #Checking if path exist function
    path = init_mas[int(num)-1]
    located = 0
    delete_file = open(del_directory, 'r')
    for line in delete_file.readlines():
        if line == path:
            located += 1
    delete_file.close()
    return located


def create_init(): #create init_mas[], which has log files from def_log.txt and log.txt
    init_mas = []
    def_log_file = open(def_log_directory, 'r')
    for line in def_log_file.readlines():#Adding def_log.txt content
        line = line.rstrip('\n')
        init_mas.append(str(line))
    log_dir = open(log_directory, 'r')
    for line in log_dir.readlines():#Adding log.txt content
        line = line.rstrip('\n')
        init_mas.append(str(line))
    return init_mas

########################SOFT DELETE FUNCTIONS#######################

def soft_delete():#empty files contents using /dev/null
    if os.path.isfile(del_directory):
        print("""\033[1;33m[!!!]Warning, after this operations this files will be cleared:\033[1;m""")
        i = 1
        del_file = open(del_directory, 'r')
        delete = []
        for path in del_file.readlines():
            path = path.rstrip('\n')
            print('['+str(i)+'] ' + path)
            delete.append(path)
            i += 1
        del_file.close()
        while True:
            ans = raw_input("""\033[1;33m[!!!]Do you want to continue?[Y/n]\033[1;m""")
            if ans == "y":
                for path in delete:
                    os.popen('cp /dev/null ' + str(path))
                os.popen('rm -f ' + del_directory)
                sys.exit("""\033[1;32m[+]Successfully cleared log file(s)!\033[1;m""")
            elif ans == "n":
                sys.exit("""\033[1;34m[*]Closing cleanx, goodbye!\033[1;m""")
    else:
        print("""\033[1;31m[-]Looks like delete.txt does not exist. Please create it in configuration mod:)\033[1;m""")
        sys.exit()

#####################GRAVE DELETE FUNCTIONS##########################################

def grave_delete():#Deleting files using rm command
    if os.path.isfile(del_directory):
        print("""\033[1;31m[!!!]Warning, after this operation this files will be DELETED:\033[1;m""")
        i = 1
        delete = []
        del_file = open(del_directory, 'r')
        for path in del_file.readlines():
            path = path.rstrip('\n')
            print('['+str(i)+'] ' + path)
            delete.append(path)
            i +=1
        del_file.close()
        while True:
            print("""\033[1;31m[!!!]Do you want to continue?[Y/n]\033[1;m""")
            ans = raw_input("""\033[1;32m[*]=> \033[1;m""")
            if ans == 'y':
                for path in delete:
                    os.popen('rm -f '+path)
                os.popen('rm -f ' + del_directory)
                sys.exit("""\033[1;32m[+]Successfully removed log file(s)!\033[1;m""")
            elif ans == 'n':
                sys.exit("""\033[1;34m[*]Closing cleanx, goodbye!\033[1;m""")
    else:
        print("""\033[1;31m[-]Looks like delete.txt does not exist. Please create it in configuration mod:)\033[1;m""")
        sys.exit()
if sys.argv[1] == '-c':
    configure()
elif sys.argv[1] == '-h':
    help()
elif sys.argv[1] == '-s':
    soft_delete()
elif sys.argv[1] == '-g':
    grave_delete()
else:
    help()

