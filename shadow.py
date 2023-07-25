# Very basic quick script to print out shadow rules from Panorama against all connected devices
#
# Very basic quick script to print out shadow rules from Panorama against all connected devices
#
# Replace the variable with your panorama IP
#
# Use the encryptapi.py scrip to encrypt the api key into non readable form (Read the instructions in that script please)
# This script will not run without ./apikey.txt and ./apipass.txt
#
# Preferrably create a virutal environment for this script
# python3 -m venv "name of virtual environment"  --> Create the Virtual Environment
# source path-to-virtual-environent/bin/activate --> Activate the virtual environment
# run pip -r requirements.txt to install the libraries required for this script
# Run the script python ./shadow.py
#
#



from os import environ
from panos.panorama import Panorama
import pprint
import pdb
from apifunctions import get_api
from cryptography.fernet import Fernet
import os

# (Replace your Panorama IP / API key here)
pano_ip = "192.168.254.5"

pan = Panorama(pano_ip, api_key=get_api())
firewalls = pan.refresh_devices(
    only_connected=True, include_device_groups=False, add=True
)
shostname = ""
mreset = True
for firewall in firewalls:
    hostname = firewall.children[0].hostname
    
    vsys = firewall.vsys
    try:
        o = firewall.op(f'show shadow-warning count vsys "{vsys}"')
        op = firewall.op(f'show shadow-warning count vsys "{vsys}"').find(".//entry")
        
        for entry in op:
            uuid = entry.attrib["uuid"]
            op = firewall.op(
                f'show shadow-warning warning-message vsys "{vsys}" uuid "{uuid}"'
            ).find(".//warning-msg")
            if shostname != hostname:
                print(f"\nFirewall {hostname} has the following shadow rules:")
                shostname = hostname
            for member in op:
                message = member.text
                print(f"\t{message}")
    except:
        print(f"\nERROR: Operational command failed to execute on {hostname}")
        pass