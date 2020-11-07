#!/usr/bin/python3
import subprocess
import os
import shlex


def change_color(x):
    cmd = f"tput setaf {x}"
    os.system(cmd)
def ask_choice():
    option = int(input("Enter your option: "))
    return option
def get_ip(interface=""):
    if not interface:
        interface = subprocess.getoutput("route | awk '/default/ {print $8}'")
    ip = subprocess.getoutput("ifconfig {0}".format(interface) + " | awk '/inet / {print $2}'")
    return ip

def docker_version():
    version = subprocess.getoutput("docker version")
    return version

def docker_info():
    info = subprocess.getoutput("docker info")
    return info

def stop_docker():
    print("Stopping docker daemon ...")
    subprocess.getoutput("systemctl stop docker")

def start_docker():
    print("Starting docker daemon ...")
    subprocess.getoutput("setenforce 0")
    subprocess.getoutput("systemctl start docker")

def get_status_docker():
    print("Fetching status ...")
    status = subprocess.getoutput("systemctl status docker")    
    return status

def list_containers():
    print("Fetching containers ...")
    containers = subprocess.getoutput("docker ps -a")
    return containers

def list_images() :
    print("Fetching docker images ...")
    images = subprocess.getoutput("docker images")
    return images

def pull_image(name):
    print("Downloading docker image {} ...".format(name))
    subprocess.getoutput("docker image pull {}".format(name))

def remove_image(name) :
    print("Removing docker image {} ...".format(name))
    subprocess.getoutput("docker image rm {}".format(name))

def launch_docker_container(image, name, detach=""):
    cmd = "docker run -dit "
    if name.strip() :
        cmd = cmd + " --name {} ".format(name)

    cmd = cmd + " {} ".format(image)
    print("Launching Container ...")
    cid = subprocess.getoutput(cmd)
    return cid

def remove_containers(name='', force=False, all_running=False, all_stopped=False):
    if name and (not force):
        print("Removing container {} ...".format(name))
        subprocess.getoutput('docker container rm {}'.format(name))
    elif force:
        print("Removing container {} forcefully ...".format(name))
        subprocess.getoutput('docker container rm -f {}'.format(name))
    elif all_running:
        print("Removing all running containers ...")
        subprocess.getoutput('docker container rm -f $(docker ps -aq)')
    elif all_stopped:
        print("Removing all stopped containers ...")
        subprocess.getoutput('docker container rm $(docker ps -aq)')

def stop_container(name):
    print("Stopping container {} ...".format(name))
    subprocess.getoutput("docker container stop {}".format(name))

def start_container(name):
    print("Starting container {} ...".format(name))
    subprocess.getoutput("docker container start {}".format(name))

def exec_command(name, cmd):
    op = subprocess.getoutput("docker container exec {} {}".format(name, cmd))
    return op

def search_image(name):
    print("Searching for {} ...".format(name))
    op = subprocess.getoutput("docker search {}".format(name))
    return op

def container_logs(name):
    print("Obtaining logs for {} ...".format(name))
    logs = subprocess.getoutput("docker logs {}".format(name))
    return logs

def copy_to_container(name, src, dest):
    print("Copying {} to Container {} at {} ...".format(src, name, dest))
    subprocess.getoutput("docker cp {} {}:{}".format(src, name, dest))

def copy_from_container(name, src, dest):
    print("Copying {} from Container {} at {} ...".format(src, name, dest))
    subprocess.getoutput("docker cp {}:{} {}".format(name, src, dest))

main_menu = ["launch a docker container", "list docker containers", 
            "remove docker containers", "stop a container",
            "start a container",
            "copy file to container", "copy file from container",
            # "attach to a container",
            "run a command on specific container", "pull an image",
            "list images", "remove image", "search for images on dockerhub",
            "check logs on a container",
            "know docker version",
            "know docker info", "custom linux command",
            "start docker daemon", "stop docker daemon", 
            "know status of docker daemon",
            "quit"
            ]

while True:
    change_color(1)
    print("\t\t\tWelcome to the menu!!!")
    change_color(7)
    print("\t\t\t-----------------------")
    print()

    for i in range(1, len(main_menu)+1):
        print("Press {} : To {}".format(i, main_menu[i-1]))

    option = ask_choice()
    option = main_menu[option-1]

    if option == "launch a docker container" :
        image = input("Enter Image name and version(centos:latest): ") or "centos"
        name = input("Enter name of the container(default- random): ")

        cid = launch_docker_container(image=image, name=name)
        print(cid)

    elif option == 'list docker containers' :
        containers = list_containers()
        print(containers)

    elif option == "remove docker containers":
        remove_containers_menu = ["remove one container", "remove one container focefully",
                                  "remove all stopped containers", "remove all containers" 
                                 ]

        for i in range(1, len(remove_containers_menu)+1):
            print("Press {} : To {}".format(i, remove_containers_menu[i-1]))
        
        option = ask_choice()
        option = remove_containers_menu[option-1]

        if option == "remove one container":
            name = input("Enter name/id of the container: ")
            remove_containers(name=name)

        elif option == "remove one container focefully":
            name = input("Enter name/id of the container: ")
            remove_containers(name=name , force=True)
        elif option == "remove all stopped containers":
            remove_containers(all_stopped=True)
        elif option == "remove all containers":
            remove_containers(all_running=True)
        else :
            print("Option not supported")

    elif option == "stop a container":
        name = input("Enter name/id of the container: ")
        stop_container(name=name)

    elif option == "start a container":
        name = input("Enter name/id of the container: ")
        start_container(name=name)
    
    elif option == "copy file to container":
        name = input("Enter name/id of the container: ")
        src = input("Enter path of source file: ")
        dest = input("Enter path of destination file: ")
        copy_to_container(name, src, dest)

    elif option == "copy file from container":
        name = input("Enter name/id of the container: ")
        src = input("Enter path of source file: ")
        dest = input("Enter path of destination file: ")
        copy_from_container(name, src, dest)

    elif option == "run a command on specific container":
        name = input("Enter name/id of the container: ")
        cmd = input("Enter a command: ")
        op = exec_command(name=name, cmd=cmd)
        print(op)
    
    elif option == "pull an image":
        name = input("Enter name and tag of the iamge: ")
        pull_image(name=name)

    elif option == "list images":
        images = list_images()
        print(images)

    elif option == "remove image":
        name = input("Enter name/id of the image: ")
        remove_image(name=name)

    elif option == "search for images on dockerhub":
        name = input("Enter search word: ")
        op = search_image(name=name)
        print(op)
        
    elif option == "check logs on a container":
        name = input("Enter contianer name/id: ")
        logs = container_logs(name)
        print(logs)

    elif option == "know docker version":
        version = docker_version()
        print(version)
    
    elif option == "know docker info":
        info = docker_info()
        print(info)

    elif option == "custom linux command":
        cmd = input("Enter custom command: ")
        op = subprocess.getoutput(cmd)
        print(op)
    
    elif option == "start docker daemon":
        start_docker()

    elif option == "stop docker daemon":
        stop_docker()

    elif option == "know status of docker daemon":
        status = get_status_docker()
        print(status)

    elif option == "quit" :
        break
    else :
        print("Option not supported")