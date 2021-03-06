import sys
from os     import system, popen
from time   import sleep


def install_os(config):
    system("vboxmanage startvm " + config["VMNAME"])
    # system("vboxmanage startvm " + config["VMNAME"] + " --type headless")
    sleep(1)
    is_running = popen("vboxmanage showvminfo " + config["VMNAME"] \
        + " | grep -c 'running'").read()
    if is_running[0] != '1':
        print("roger_skyline_1: Can't run VM " + config["VMNAME"], file=sys.stderr)
        exit()
    else:
        print("Installing Operating System to VM " + config["VMNAME"])
        while True:
            is_running = popen("vboxmanage showvminfo " + config["VMNAME"] \
                + " | grep -c 'running'").read()
            if is_running[0] == '1':
                sleep(5)
            else:
                print("Operating System Installed")
                break
        system("vboxmanage storageattach " + config["VMNAME"] \
            + " --storagectl IDE --port 0 --device 0 --medium none")
