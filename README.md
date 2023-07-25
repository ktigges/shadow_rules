shadow_rules

Very basic quick script to print out shadow rules from Panorama against all connected devices



Modify shadow.py and replace the variable with your panorama IP

Use the encryptapi.py script to encrypt the api key into non readable form (Read the instructions in that script please)

This script will not run without ./apikey.txt and ./apipass.txt

Preferrably create a virutal environment for this script
- python3 -m venv "name of virtual environment"  --> Create the Virtual Environment
- source path-to-virtual-environent/bin/activate --> Activate the virtual environment
- run pip -r requirements.txt to install the libraries required for this script
- Run the script python ./shadow.py