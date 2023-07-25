from cryptography.fernet import Fernet
import os

def get_api():
    cwd = './'
    with open('./apipass.txt') as f:
        apipwd = ''.join(f.readlines())
        encpwdbyt = bytes(apipwd, 'utf-8')
    f.close()

    # read key and convert into byte
    with open('./apikey.txt') as f:
        refKey = ''.join(f.readlines())
        refKeybyt = bytes(refKey, 'utf-8')
    f.close()

    # use the key and decrypt the password

    keytouse = Fernet(refKeybyt)
    # Convert the password from byte to Ascii
    api_key = (keytouse.decrypt(encpwdbyt)).decode('ASCII')
    return api_key.strip()


def returnheader(api_key):
# Functions returns the "Authorization Basic" header with the userid:password encoded in base64
#
    #authstr = user_id + ":" + user_password
    #bytestr = authstr.encode('ascii')
    #authb64 = base64.b64encode(bytestr)
    #authb64 = str(authb64, encoding='utf-8')

    header = { 'X-PAN-KEY' : f'{api_key}'}
    return(header)