from linux_cmds import *
from lvm_commands import *

main_menu = ["create an folder", "show present directory", 
            "show ip address", "show date",
            "show calender", "create cmd",
            "install pkg", "remote cli",
            "ping address", 
            "show current user information", 
            "show packet information",
            "show cpu details",
            "shutdown", "reboot", 
            "show current memory usage",
            "show running process", 
            "show all using port in system", 
            "mycomputer", "LVM",
            "quit"
            ]

while True:
    change_color(1)
    print("\t\t\tWelcome to Linux Command menu!!!")
    change_color(7)
    print("\t\t\t-----------------------")
    print()

    for i in range(1, len(main_menu)+1):
        print("Press {} : To {}".format(i, main_menu[i-1]))

    option = ask_choice()
    option = main_menu[option-1]

    if option == "create an folder" :
        name = input("Enter the file name (default name 'newfolder') : ") or "newfolder"
        mkdir(name) 

    elif option == "show present directory" :
        pwd = pwd()
        print(pwd)

    elif option == "show ip address" :
        ifconfig = ifconfig()
        print(ifconfig)

    elif option == "show date" :
        date = date()
        print(date)
        
    elif option == "show calender" :
        cal = cal()
        print(cal)

    elif option == "create cmd" :
        name = input("Enter the new name of cmd (default name 'newcmd') : ") or "newcmd"
        work = input("define the fuction of cmd (default function 'echo linux') : ") or "echo linux"
        alias(name,work)
        
        
    elif option == "install pkg" :
        name = input("Enter the pkg name (default name 'figlet') : ") or "figlet"
        yum(name)
        

    elif option == "remote cli" :
        ip = input("Enter the ip address (default name '127.0.0.1') : ") or "127.0.0.1"
        ssh = ssh(ip)
        print(ssh)

    elif option == "ping address" :
        ip = input("Enter the ip address (default name '127.0.0.1') : ") or "127.0.0.1"
        ping(ip)
            

    elif option == "show current user information" :
        whoami = whoami()
        print(whoami)

    elif option == "show packet information" :
        tcpdump = tcpdump()
        print(tcpdump)
        
    elif option == "show cpu details" :
        lscpu = lscpu()
        print(lscpu)

    elif option == "shutdown" :
        inits()
        
    elif option == "reboot" :
        initr()

    elif option == "show current memory usage" :
        free = free()
        print(free)

    elif option == "show running process" :
        ps = ps()
        print(ps)
        
    elif option == "show all using port in system" :
        netstat = netstat()
        print(netstat)

    elif option == "mycomputer" :
        mycomputer = mycomputer()
        print(mycomputer)

    elif option == "LVM" :
        os.system("fdisk -l")
        vol_dir = input("Enter the path of volume (default - /dev/sdb) : ") or "/dev/sdb"
        name_vol = input("Enter the name of vol (default name 'deadlock'):") or "deadlock"
        lvm(vol_dir,name_vol)
        
    elif option == "quit" :
        break
    else :
        print("Option not supported")