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
    print("\t\t\tWelcome to LVM menu!!!")
    change_color(7)
    print("\t\t\t-----------------------")
    print()

    for i in range(1, len(main_menu)+1):
        print("Press {} : To {}".format(i, main_menu[i-1]))

    option = ask_choice()
    option = main_menu[option-1]
    

    if option == "create a PV" :
        os.system('clear')
        device_name = input("Enter the device name (default- /dev/sda) : ") or "/dev/sda"
        op = create_pv(device_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "list all the PVs" :
        op = list_all_pvs()
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "get details of a PV" :
        os.system('clear')
        pv_name = input("Enter the PV name: ")
        op = list_pv(pv_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "remove a PV" :
        os.system('clear')
        pv_name = input("Enter the PV name: ")
        op = remove_pv(pv_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "remove a VG" :
        os.system('clear')
        vg_name = input("Enter the VG name: ")
        op = remove_vg(vg_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "remove an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        op = remove_lv(lv_name)
        input("Press Enter to continue")
        os.system('clear')
        

    elif option == "create a VG" :
        os.system('clear')
        pv_name = input("Enter the PV name: ")
        vg_name = input("Enter the VG name:(default- auto) ") or "auto"
        op = create_vg(vg_name, pv_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "list all the VGs" :
        op = list_all_vgs()
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "get details of a VG" :
        os.system('clear')
        vg_name = input("Enter the VG name: ")
        op = list_vg(vg_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')
        
    elif option == "extend a VG" :
        os.system('clear')
        pv_name = input("Enter the PV name: ")
        vg_name = input("Enter the VG name: ")
        op = extend_vg(vg_name, pv_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')
        

    elif option == "create a LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")
        size = input("Enter the size for LV: ")
        op = create_lv(size, lv_name, vg_name)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "list all the LVs" :
        op = list_all_lvs()
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "get details of an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")
        
        op = list_lv(vg_name, lv_name)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "format an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")

        lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
        op = format_lv(lv_path)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "mount an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")

        lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
        mount_path = input("Enter the path to mount the LV: ")
        op = mount_lv(lv_path, mount_path)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        print("Mounted Successfully")
        input("Press Enter to continue")
        os.system('clear')

    elif option == "extend an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")

        lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
        size = input("Enter the size by which LV should extend: ")

        op = extend_lv(size, lv_path)
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "reduce an LV" :
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")

        lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
        size = input("Enter the new size: ")
        mount_path = input("Enter the new mount point: ")

        op = reduce_lv_and_format(size, lv_path, mount_path)
        print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "unmount an LV":
        os.system('clear')
        lv_name = input("Enter the LV name: ")
        vg_name = input("Enter the VG name: ")

        lv_path = f"/dev/mapper/{vg_name}-{lv_name}"
        op = unmount_lv(lv_path)
        os.system('clear')
        os.system("Unmounted Successfully")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "display the disk space" :
        op = disk_space()
        os.system('clear')
        os.system(f"echo '{op}' | more")
        # print(op)
        input("Press Enter to continue")
        os.system('clear')

    elif option == "create a directory":
        os.system('clear')
        dir_path = input("Enter the path to directory: ")
        op = mkdir(dir_path)

    elif option == "quit" :
        break
    else :
        print("Option not supported")


# automate /dev/mapper/testvg-lv1