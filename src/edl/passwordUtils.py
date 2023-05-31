import re
import getpass

def validate_password_format(pwdin):
    _err_list = []
    if len(pwdin) < 8:
        _err_list.append('password must be at least 8 chars long')
        # yield 'password must be at least 8 chars long'

    _bl_upper = False
    _bl_lower = False
    for el in pwdin:
        if el.isupper():
            _bl_upper = True
        if el.islower():
            _bl_lower = True
        if _bl_upper and _bl_lower:
            break

    if _bl_lower is False or _bl_upper is False:
        _err_list.append('password must contain upper and lower letters')
        # yield 'password must contain upper and lower letters'

    if re.search('[£$%&#+*@\/\\%!]', pwdin) is None:
        _err_list.append('password must contain at least one special char *?^!£$%&/()+-#=')
        # yield 'password must contain at least one special char *?^!£$%&/()+-#='
    
    if re.search('[0-9]', pwdin) is None:
        _err_list.append('password must contain at least one number')    
        # Syield 'password must contain at least one number'

    return _err_list

'''
class for managing encryption
'''
class EncrObj:
    def __init__(self) -> None:
        self.password_provided = None
        self.key = None
        self.filename = None
        self.operation = None


'''
function to ask and store the password
'''
def ask_for_pwd(encrObj):
    while True: 
        encrObj.password_provided  = getpass.getpass('Enter password: ')
        password_validation = validate_password_format(encrObj.password_provided)    
        for val in password_validation:
            print(val)
        if len(password_validation) == 0:
            break

    while True:
        password_provided_check =  getpass.getpass('Re-enter password, q for exit: ')
        exit_prg(password_provided_check)       
        if encrObj.password_provided != password_provided_check:
            print('Password does not match')
        else:
            break


'''
function to ask the option (encrypt or decrypt)
'''
def as_for_opt(encrObj):
    while True:
        encrObj.operation = input('e to encrypt, d for decrypt, q for exit: ')
        exit_prg(encrObj.operation)
        if encrObj.operation != 'e' and encrObj.operation != 'd':
            print("Invalid option")
        else:
            break    

def exit_prg(keypress):
    if keypress == 'q':
        exit()  