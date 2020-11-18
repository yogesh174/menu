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
    os.system("mkdir /{}".format(name_dir))
    os.system("mount {} /{} ".format(vol_dir,name_dir))
    a = os.system("cd /{} ".format(name_dir))
    return a