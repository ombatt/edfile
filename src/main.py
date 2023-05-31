import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from edl.passwordUtils import *
from edl.generateKey import *
from edl.encrypt import *
import sys
    
'''
begin the function
'''
encrObj = EncrObj()

'''
ask for all the information
'''
ask_for_pwd(encrObj)
as_for_opt(encrObj)
generate_key(encrObj)

if sys.argv is None or len(sys.argv) <= 1:
    encrObj.filename = input('file name: ')
else:
    encrObj.filename = sys.argv[1]
'''
iterate until the file is encrypted or decrypted
'''
success = True
while success:
    try:
        if encrObj.operation == 'e':
            encrypt(encrObj)
        elif encrObj.operation == 'd':
            decrypt(encrObj)
        success = False
        print("operation completed successfully")
    except Exception as ex:
        ask_for_pwd(encrObj)
        generate_key(encrObj)    


    