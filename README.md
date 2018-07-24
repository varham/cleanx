# CLEANX 
Cleanx is a tool for cleaning Linux log files. It has three differrent mods - configuration mode, soft delete mode and grave delete mode.
# INSTALLATION
You can download cleanx by cloning Git repository:
 ```
 git clone https:/github.com/varham/cleanx
 ```
  
After cloning, type ```cd cleanx```  in your terminal and run install.py as root
Cleanx works with Python version 2.7.x on any platform
# USAGE

```sudo python cleanx.py -mode_name```

# MODE DESCRIPTION
Configuration mode - can be used to add your own log files or for the configuration of the delete.txt file. Delete.txt is file, where all pathes of your log files are stored. The program deletes only those files, which are located in this file. You can add new directoires to it or remove existing with the help of configuration mode. To use this mode, use -c argument

Soft delete mode - empty the contents of every file, located in delete.txt using cp /dev/null command. To use this mode  use -s argument

Grave delete mode - delete every log file from delete.txt from your computer using rm command. To use this mode use -g argument
# PLANS FOR FUTURE
Some logs located not only in one file - sometimes there are different files with the same content or the copy of log file is located in archive. The next target is to add support for cleaning this files.
# OFFERS
If you have any offers or suggestions or you found out an error or a bug - please write to my email - varhamov@gmail.com or write directly in GitHub. Thank you!

