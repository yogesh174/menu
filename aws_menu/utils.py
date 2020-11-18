import subprocess
import os
import shlex
import boto3
import json
import datetime
import pandas as pd
import time
from subprocess import check_call

def change_color(x):
    cmd = "tput setaf {}".format(x)
    os.system(cmd)
def ask_choice():
    option = int(input("Enter your option: "))
    return option
def get_ip(interface=""):
    if not interface:
        interface = subprocess.getoutput("route | awk '/default/ {print $8}'")
    ip = subprocess.getoutput("ifconfig {0}".format(interface) + " | awk '/inet / {print $2}'")
    return ip
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)

