# edfile
Script to encript and decript files with password.

INSTRUCTIONS:
1) Run the main.py file. It is possible to pass the file name to encrypt/decrypt as an argument.
2) Once encrypted the original file will be deleted and a new encrypted file will be created with .enc extension
3) Once decrypted the .enc file will be deleted and the original file will per saved

- It is recommended to change the byte string "salt" in generateKey.py file. 
- It is possibile to convert in exe file with pyinstaller.
