from cryptography.fernet import Fernet
import os

from edl.passwordUtils import exit_prg

def encrypt(encrObj):
    '''# opening the key
    with open('key.key', 'rb') as filekey:
        key = filekey.read()'''
    try:
        # using the generated key
        fernet = Fernet(encrObj.key)
        
        # opening the original file to encrypt
        with open(encrObj.filename, 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and
        # writing the encrypted data
        with open(encrObj.filename + ".enc", 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        os.remove(encrObj.filename)

    except Exception as ex:
        print(ex)
        raise ex

def decrypt(encrObj):

    if encrObj.filename[-3:] != "enc":
        print("file extension not correct")
        exit_prg("q")

    try:
        # using the generated key
        fernet = Fernet(encrObj.key)

        # opening the encrypted file
        with open(encrObj.filename, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(encrObj.filename[:-4], 'wb') as dec_file:
            dec_file.write(decrypted)     

        os.remove(encrObj.filename)

    except Exception as ex:
        print("error decrypting file, check password")
        raise ex   