import subprocess

interface = input("Interface > ")
new_mac = input("New MAC > ")

if not interface:
    print("Please enter an interface")
    exit()
elif not new_mac:
    print("Please enter a MAC address")
    exit()

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

ifconfig_result = subprocess.check_output("ifconfig " + interface, shell=True)

print(ifconfig_result)
