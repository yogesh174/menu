from linux_cmds import *
from lvm_commands import *

main_menu = ["create a PV", "list all the PVs", 
            "get details of a PV",
            "remove a PV",
            "create a VG",
            "list all the VGs", "get details of a VG",
            "extend a VG", 
            "remove a VG",
            "create a LV",
            "list all the LVs", 
            "get details of an LV",
            "format an LV",
            "mount an LV",
            "extend an LV",
            "reduce an LV",
            "unmount an LV",
            "remove an LV",
            "display the disk space",
            "create a directory",
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
    

    if option == "create a PV" :
        device_name = input("Enter the device name (default- /dev/sda) : ") or "/dev/sda"
        op = create_pv(device_name)
        print(op)

    elif option == "list all the PVs" :
        op = list_all_pvs()
        print(op)

    elif option == "get details of a PV" :
        pv_name = input("Enter the PV name: ")
        op = list_pv(pv_name)
        print(op)

    elif option == "remove a PV" :
        pv_name = input("Enter the PV name: ")
        op = remove_pv(pv_name)
        print(op)

    elif option == "remove a VG" :
        vg_name = input("Enter the VG name: ")
        op = remove_vg(vg_name)
        print(op)

    elif option == "remove an LV" :
        lv_name = input("Enter the LV name: ")
        op = remove_lv(lv_name)
        print(op)
        

    elif option == "create a VG" :
        pv_name = input("Enter the PV name: ")
        vg_name = input("Enter the VG name:(default- auto) ") or "auto"
        op = create_vg(vg_name, pv_name)
        print(op)

    elif option == "list all the VGs" :
        op = list_all_vgs()
        print(op)

    elif option == "get details of a VG" :
        vg_name = input("Enter the VG name: ")
        op = list_vg(vg_name)
        print(op)
        
    elif option == "extend a VG" :
        pv_name = input("Enter the PV name: ")
        vg_name = input("Enter the VG name: ")
        op = extend_vg(vg_name, pv_name)
        print(op)
        

    elif option == "create a LV" :
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")
        size = input("Enter the size for LV: ")
        op = create_lv(size, lv_name, vg_name)
        print(op)

    elif option == "list all the LVs" :
        op = list_all_lvs()
        print(op)

    elif option == "get details of an LV" :
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")
        
        op = list_lv(vg_name, lv_name)
        
        print(op)

    elif option == "format an LV" :
        lv_path = input("Enter the path for LV: ")
        op = format_lv(lv_path)
        print(op)

    elif option == "mount an LV" :
        lv_path = input("Enter the path for LV: ")
        mount_path = input("Enter the path to mount the LV: ")
        op = mount_lv(lv_path, mount_path)
        print(op)

    elif option == "extend an LV" :
        lv_path = input("Enter the path for LV: ")
        size = input("Enter the size by which LV should extend: ")

        op = extend_lv(size, lv_path)
        print(op)

    elif option == "reduce an LV" :
        lv_path = input("Enter the path for LV: ")
        size = input("Enter the new size: ")
        mount_path = input("Enter the new mount point: ")

        op = reduce_lv_and_format(size, lv_path, mount_path)
        print(op)

    elif option == "unmount an LV":
        lv_path = input("Enter the path for LV: ")
        op = unmount_lv(lv_path)
        print(op)

    elif option == "display the disk space" :
        op = disk_space()
        print(op)

    elif option == "create a directory":
        dir_path = input("Enter the path to directory: ")
        op = mkdir(dir_path)
        print(op)

    elif option == "quit" :
        break
    else :
        print("Option not supported")


# automate /dev/mapper/testvg-lv1
