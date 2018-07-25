#-*- coding: utf-8 -*-
import os
import sys
from variables import Colors
from variables import Variables as v


 # Checking if cleanx is running as root
if not os.geteuid() == 0:
    print(Colors.YELLOW + "[!]You must run script as root" + Colors.COLOR_END)
    sys.exit()


##Help function
def help():
    print(Colors.GREEN +
  """      
[ -c ] ------ Configuration mode (Add log file(s) path, configure delete.txt)
[ -s ] ------ Soft mode (Remove content of files with /dev/null)
[ -g ] ------ Grave mode (Delete files from computer)
  """ + Colors.COLOR_END
    )

################CONFIGURATION MOD FUNCTIONS######################################

def configure():
    if os.path.isfile(v.def_log_directory):
        file = open(v.def_log_directory, 'r')
        for line in file.readlines():
            line = line.rstrip('\n')
            r = 0
            for path in v.default_log_dir:
                if line == path:
                    r += 1
                else:
                    pass
            if r < 1:
                def_file = open(v.def_log_directory, 'a')
                def_file.write(path+'\n')
                def_file.close()
    else:
        for path in v.default_log_dir:
            if os.path.isfile(path):
                def_file = open(v.def_log_directory, 'a')
                def_file.write(path+'\n')
                def_file.close()
    print(Colors.WHITE + """
     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗██╗  ██╗
    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║╚██╗██╔╝
    ██║     ██║     █████╗  ███████║██╔██╗ ██║ ╚███╔╝ 
    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║ ██╔██╗ 
    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║██╔╝ ██╗
     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ 
                      [Cleanx v1.0             ] 
                      [Configuration mode      ] 
                      [Author:varham           ]   
                      [Mail: varhamov@gmail.com]   """ + Colors.COLOR_END
                                                     )  # Banner
    menu()


def menu():  # Main menu function
    print(Colors.BLUE + """
########################################################
[*]Choose configure option:
[1] - Add log file
[2] - Configure delete.txt
[3] - Exit
#########################################################
     """ + Colors.COLOR_END)
    option = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
    if option == "1":
        add_log()
    elif option == "2":
        conf()
    elif option == "3":
        sys.exit()

def add_log():  # Add log function
    print(Colors.WHITE + "[*]Enter log file directory (e.g. /home/user/folder/log).Type 'back' to return to main menu" + Colors.COLOR_END)
    directory = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
    if directory.lower() == 'back':
        menu()
    if os.path.isfile(directory):  # If file exist, adding it to log.txt
        log_file = open(v.log_directory, 'a')
        log_file.write(directory+'\n')
        log_file.close()
        print(Colors.GREEN + "[+]Succesfully added log file directory!" + Colors.COLOR_END)
        menu()
    else:  # If file does not exits, call add_log again
        print(Colors.RED + "[-]Can't add log file path. Please check if directory is correct or if the file exist and try again" + Colors.COLOR_END)
        add_log()


def conf(): #delete.txt configuration menu function
    if os.path.isfile(v.del_directory):
        print(Colors.BLUE + """
#########################################################
[*]Choose next configuration step:
[1] - Add new file directories to delete.txt
[2] - Remove file directories from delete.txt
[3] - Delete delete.txt
[4] - Return to main menu
#########################################################
        """ + Colors.COLOR_END)
        option = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
        if option.lower == 'back' or option == "4":
            menu()
        elif option == "1":
            add()
        elif option == "2":
            remove()
        elif option == "3":
            os.popen("rm -f " + v.del_directory)
            print(Colors.GREEN + "[+]Successfully removed delete.txt!" + Colors.COLOR_END)
            menu()
    else:
        print(Colors.YELLOW + "[!]Delete.txt does not exist. Do you want to create one?[Y/n]" + Colors.COLOR_END)
        ans = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
        if ans.lower() == 'y':
            add()
        elif ans.lower == 'n':
            menu()


def add(): #Add new logs to delete.txt function
    init_mas = create_init()
    print(Colors.WHITE + "[*]Choose log files you want to add to delete.txt(e.g. 1,2,4,6 or 1-8)" + Colors.COLOR_END)
    i = 1
    for item in init_mas:#print all logs path from all files (def_log.txt, log.txt)
        print ('['+str(i)+'] ' + item)
        i+=1
    files = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
    del_file = open(v.del_directory, 'a')
    if files == "back":
        conf()
    elif ',' in files:
        files = files.split(',')#split user input to get indexes of logs
        for num in files:
            located = check_path(num, init_mas)#check if the path exists in the file
            if located < 1: #if not, adding path to file
                del_file.write(init_mas[int(num)-1]+"\n")
        del_file.close()
        print(Colors.GREEN + "\n[+]Successfully added log file directories!" + Colors.COLOR_END)
        conf()
    elif '-' in files:
        files = files.split('-')#split user input to get indexes of logs
        for num in range(int(files[0]), int(files[1])+1):
            located = check_path(num, init_mas)#check if the path exists in the file
            if located < 1:#if not, adding path to file
                del_file.write(init_mas[int(num)-1]+"\n")
        del_file.close()
        print(Colors.GREEN + "\n[+]Successfully added log file directories!" + Colors.COLOR_END)
        conf()
    else:
        del_file.write(init_mas[int(files)-1])
        del_file.close()
        print(Colors.GREEN + "[1;32m\n[+]Successfully added log file directories!" + Colors.COLOR_END)
        conf()

def remove():  #Remove logs from delete.txt function
    del_buf = []
    del_file = open(v.del_directory, 'r')
    for line in del_file.readlines():
        line = line.rstrip('\n')
        del_buf.append(line)  #Reading all content from delete.txt and appending it ro def_buf[]
    del_file.close()
    print(Colors.WHITE + "[*]Choose log files you want to remove from delete.txt(e.g. 1,2,4,6 or 1-8)" + Colors.COLOR_END)
    i = 1
    for path in del_buf:
        print('[' + str(i) + '] ' + path)  #Printing delete.txt content
        i += 1
    files = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
    if files == 'back':
        conf()
    elif ',' in files:
        files = files.split(',')
        for num in files:
            del_buf[int(num)-1] = None #Removing content
        del_buf = filter(None, del_buf)
        print del_buf
        print(Colors.GREEN + "\n[+]Successfully remove log file directories!" + Colors.COLOR_END)
        os.popen("rm -f " + v.del_directory)  #Removing delete.txt
        del_file = open(v.del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')  # Creating delete.txt and write remaining content to it
        del_file.close()
        conf()
    elif '-' in files:
        files = files.split('-')
        for num in range(int(files[0]), int(files[1])+1):
            del_buf[int(num)-1] = None #Removing content
        del_buf = filter(None, del_buf)
        print(Colors.GREEN + "\n[+]Successfully remove log file directories!" + Colors.COLOR_END)
        os.popen("rm -f " + v.del_directory)#Removing delete.txt
        del_file = open(v.del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')  # Creating delete.txt and write remaining content to it
        del_file.close()
        conf()
    else:
        del del_buf[int(files)-1]
        os.popen("rm -f delete.txt")
        del_file = open(v.del_directory, 'a')
        for path in del_buf:
            del_file.write(path+'\n')
        del_file.close()
        print(Colors.GREEN + "\n[+]Successfully remove log file path!" + Colors.COLOR_END)
        conf()


def check_path(num, init_mas):  #Checking if path exist function
    path = init_mas[int(num)-1]
    located = 0
    delete_file = open(v.del_directory, 'r')
    for line in delete_file.readlines():
        if line == path:
            located += 1
    delete_file.close()
    return located


def create_init(): #create init_mas[], which has log files from def_log.txt and log.txt
    init_mas = []
    def_log_file = open(v.def_log_directory, 'r')
    for line in def_log_file.readlines():#Adding def_log.txt content
        line = line.rstrip('\n')
        init_mas.append(str(line))
    log_dir = open(v.log_directory, 'r')
    for line in log_dir.readlines():#Adding log.txt content
        line = line.rstrip('\n')
        init_mas.append(str(line))
    return init_mas

########################SOFT DELETE FUNCTIONS#######################

def soft_delete():#empty files contents using /dev/null
    if os.path.isfile(v.del_directory):
        print(Colors.YELLOW + "[!!!]Warning, after this operations this files will be cleared:" + Colors.COLOR_END)
        i = 1
        del_file = open(v.del_directory, 'r')
        delete = []
        for path in del_file.readlines():
            path = path.rstrip('\n')
            print('['+str(i)+'] ' + path)
            delete.append(path)
            i += 1
        del_file.close()
        while True:
            print(Colors.YELLOW + "[!!!]Do you want to continue?[Y/n]" + Colors.COLOR_END)
            ans = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
            if ans == "y":
                for path in delete:
                    os.popen('cp /dev/null ' + str(path))
                os.popen('rm -f ' + v.del_directory)
                sys.exit(Colors.GREEN + "[+]Successfully cleared log file(s)!" + Colors.COLOR_END)
            elif ans == "n":
                sys.exit(Colors.BLUE + "[*]Closing cleanx, goodbye!" + Colors.COLOR_END)
    else:
        print(Colors.RED + "[-]Looks like delete.txt does not exist. Please create it in configuration mod:)" + Colors.COLOR_END)
        sys.exit()

#####################GRAVE DELETE FUNCTIONS##########################################

def grave_delete():#Deleting files using rm command
    if os.path.isfile(v.del_directory):
        print(Colors.RED + "[!!!]Warning, after this operation this files will be DELETED:" + Colors.COLOR_END)
        i = 1
        delete = []
        del_file = open(v.del_directory, 'r')
        for path in del_file.readlines():
            path = path.rstrip('\n')
            print('['+str(i)+'] ' + path)
            delete.append(path)
            i +=1
        del_file.close()
        while True:
            print(Colors.RED + "[!!!]Do you want to continue?[Y/n]" + Colors.COLOR_END)
            ans = raw_input(Colors.GREEN + "[*]=> " + Colors.COLOR_END)
            if ans == 'y':
                for path in delete:
                    os.popen('rm -f '+path)
                os.popen('rm -f ' + v.del_directory)
                sys.exit(Colors.GREEN + "[+]Successfully removed log file(s)!" + Colors.COLOR_END)
            elif ans == 'n':
                sys.exit(Colors.BLUE + "[*]Closing cleanx, goodbye!" + Colors.COLOR_END)
    else:
        print(Colors.RED + "[-]Looks like delete.txt does not exist. Please create it in configuration mod:)" + Colors.COLOR_END)
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

