import os

def ask_choice():
    option = int(input("Enter your option: "))
    return option


def change_color(x):
    cmd = f"tput setaf {x}"
    os.system(cmd)


def mkdir(name):
    
    a = os.system("mkdir {}".format(name))
    return a

def pwd():
    a = os.system("pwd")
    return a

def ifconfig():
    a = os.system("ifconfig")
    return a

def date():
    a = os.system("date")
    return a

def cal():
    a = os.system("cal")
    return a

def alias(name,work):
    a = os.system("alias {}='{}'".format(name,work))
    return a

def yum(name):
    a = os.system("yum install {}".format(name))
    return a


def ssh(ip):
    a = os.system("ssh {}".format(ip))
    return a


def whoami():
    a = os.system("whoami")
    return a

def tcpdump():
    a = os.system("tcpdump")
    return a

def lscpu():
    a = os.system("lscpu")
    return a

def inits():
    a = os.system("init 0")
    return a

def initr():
    a = os.system("init 6")
    return a

def free():
    a = os.system("free -m")
    return a

def ps():
    a = os.system("ps -aux")
    return a

def netstat():
    a = os.system("netstat -tnlp")
    return a

def ping(ip):
    a = os.system("ping {}".format(ip))
    return a

def mycomputer():
    a = os.system("df -h")
    return a

def lvm(vol_dir,name_dir):
    
    os.system("pvcreate {}".format(vol_dir))
    os.system("fdisk {}".format(vol_dir))
    os.system("mkfs.ext4 {}".format(vol_dir))
    os.system("mkdir /{}".format(name_vol))
    os.system("mount {} /{} ".format(vol_dir,name_vol))
    a = os.system("cd /{} ".format(name_vol))
    return a


main_menu = ["create an folder", "show present directory", 
            " show ip address", " show date",
            "show calender",
            "create cmd",
            "install pkg",
            "remote cli",
            "ping address", "show current user information", "show packet information",
            "show cpu details",
            "shutdown",
            "reboot", "show current memory usage",
            "show running process", "show all using port in system", 
            "mycomputer",
            "LVM",
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

    if option == main_menu[0] :
        name = input("Enter the file name (default name 'newfolder') : ") or "newfolder"
        mkdir(name) 

    elif option == main_menu[1] :
        pwd = pwd()
        print(pwd)

    
    elif option == main_menu[2] :
        ifconfig = ifconfig()
        print(ifconfig)

    elif option == main_menu[3] :
        date = date()
        print(date)
        
    elif option == main_menu[4] :
        cal = cal()
        print(cal)

    elif option == main_menu[5] :
        name = input("Enter the new name of cmd (default name 'newcmd') : ") or "newcmd"
        work = input("define the fuction of cmd (default function 'echo linux') : ") or "echo linux"
        alias(name,work)
        
        
    elif option == main_menu[6] :
        name = input("Enter the pkg name (default name 'figlet') : ") or "figlet"
        yum(name)
        

    elif option == main_menu[7] :
        ip = input("Enter the ip address (default name '127.0.0.1') : ") or "127.0.0.1"
        ssh = ssh(ip)
        print(ssh)

    elif option == main_menu[8] :
        ip = input("Enter the ip address (default name '127.0.0.1') : ") or "127.0.0.1"
        ping(ip)
            

    elif option == main_menu[9] :
        whoami = whoami()
        print(whoami)

    elif option == main_menu[10] :
        tcpdump = tcpdump()
        print(tcpdump)
        
    elif option == main_menu[11] :
        lscpu = lscpu()
        print(lscpu)

    elif option == main_menu[12] :
        inits()
        
        
    elif option == main_menu[13] :
        initr()

   
    elif option == main_menu[14] :
        free = free()
        print(free)

    elif option == main_menu[15] :
        ps = ps()
        print(ps)
        
    elif option == main_menu[16] :
        netstat = netstat()
        print(netstat)

    elif option == main_menu[17] :
        mycomputer = mycomputer()
        print(mycomputer)

    elif option == main_menu[18] :
        os.system("fdisk -l")
        vol_dir = input("Enter the path of volume (default - /dev/sdb) : ") or "/dev/sdb"
        name_vol = input("Enter the name of vol (default name 'deadlock'):") or "deadlock"
        lvm(vol_dir,name_vol)
        
    elif option == "quit" :
        break
    else :
        print("Option not supported")

