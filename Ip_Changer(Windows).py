import subprocess
import re

print('Type in recommended stuff to avoid any mess. This is for WIFI only')
new_ip = input('New IP (Must have the format: 10.168.22.XX) > ')

ip_check = re.findall(r'\d{2}.\d{3}.\d{2}.\d{1,3}', new_ip)

if not ip_check:
    print('Put the correct format')
    exit()

subnet_mask = input('Enter the subnet mask (Recommended: 255.0.0.0) > ')

sub_check = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d', subnet_mask)

if not sub_check:
    print('Put the correct format.')
    exit()
default_gateway = input('Default Gateway (Recommended: 10.168.22.1) > ')

gateway_check = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d', default_gateway)

if not gateway_check:
    print('Put the correct format.')
    exit()

subprocess.run('netsh interface ip set address name= "Wi-Fi" static' + new_ip + subnet_mask + default_gateway, shell=True)