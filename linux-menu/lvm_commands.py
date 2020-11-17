import subprocess
import os 

def create_pv(device_name):
    op = subprocess.getoutput("pvcreate {}".format(device_name))
    return op

def list_all_pvs():
    op = subprocess.getoutput("pvdisplay")
    return op

def list_pv(pv_name):
    op = subprocess.getoutput("pvdisplay {}".format(pv_name))
    return op

def remove_pv(pv_name):
    op = subprocess.getoutput("pvremove {}".format(pv_name))
    return op

def remove_vg(vg_name):
    op = subprocess.getoutput("vgremove {}".format(vg_name))
    return op

def remove_lv(lv_name):
    op = os.system("lvremove {}".format(lv_name))
    return op


# TODO: Create a VG with multiple pv_names 
def create_vg(vg_name, pv_name):
    op = subprocess.getoutput("vgcreate {} {}".format(vg_name, pv_name))
    return op

def list_all_vgs():
    op = subprocess.getoutput("vgdisplay")
    return op

def list_vg(vg_name):
    op = subprocess.getoutput("vgdisplay {}".format(vg_name))
    return op

def extend_vg(vg_name, pv_name):
    op = subprocess.getoutput("vgextend {} {}".format(vg_name, pv_name))
    return op

def create_lv(size, lv_name, vg_name):
    op = os.system("lvcreate --size {} --name {} {}".format(size, lv_name, vg_name))
    return op

def list_all_lvs():
    op = subprocess.getoutput("lvdisplay")
    return op

def list_lv(vg_name, lv_name):
    op = subprocess.getoutput("lvdisplay {}/{}".format(vg_name, lv_name))
    return op

# TODO: 
# 1. Auto extract the path name from a given lv name
# 2. Give a choice for type of formatting instead of default ext4
def format_lv(lv_path):
    op = subprocess.getoutput("mkfs.ext4 {}".format(lv_path))
    return op

def mount_lv(lv_path, mount_path):
    op = subprocess.getoutput("mount {} {}".format(lv_path, mount_path))
    return op

def unmount_lv(lv_path):
    op = subprocess.getoutput("umount {}".format(lv_path))
    return op

# TODO: Give a choice for dynamic units instead of only GBs 
def extend_lv(size, lv_path):
    op = subprocess.getoutput("lvextend --size +{} {}".format(size, lv_path))
    subprocess.getoutput("e2fsck -f {}".format(lv_path))
    subprocess.getoutput("resize2fs {}".format(lv_path))
    return op

def reduce_lv_and_format(new_size, lv_path, mount_path):
    os.system("umount {}".format(lv_path))
    os.system("e2fsck -f {}".format(lv_path))
    os.system("resize2fs {} {}".format(lv_path, new_size))
    os.system("lvreduce --size {} {}".format(new_size, lv_path))
    os.system("mount {} {}".format(lv_path, mount_path))
    return "Reduced LV to {}".format(new_size)

# Displays disk information for all the file systems
def disk_space():
    op = subprocess.getoutput("df -h")
    return op
