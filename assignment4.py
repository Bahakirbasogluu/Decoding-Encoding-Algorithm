import math,sys
from copy import deepcopy
class Error(Exception):
    pass
class ParameterError(Error):
    pass
class UndefinedParameterError(Error):
    pass
class InputfileisemptyError(Error):
    pass
class KeyfileemptyError(Error):
    pass
class PermissionError(Error):
    pass
letter_number_dict = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16","Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24","Y":"25","Z":"26"," ":"27"}
def enc():
    global result,encrypted_list,n,letter_to_number
    for x in range(len(letter_to_number)):
        for y in range(len(key_nxn)):
            for z in range(sqrt_clear_keys):
                result = result + letter_to_number[x][z] * key_nxn[y][z]
            encrypted_list.append(result)
            result = 0
    return encrypted_list
def dec():
    global inverse_matris,diagonal_line,temp,birim_matris,decrypted_list
    for i in range(sqrt_clear_keys):
        diagonal_line = inverse_matris[i][i]
        for j in range(sqrt_clear_keys):
            birim_matris[i][j] = birim_matris[i][j] / diagonal_line
            inverse_matris[i][j] = inverse_matris[i][j] / diagonal_line
        for k in range(sqrt_clear_keys):
            if k != i:
                temp = inverse_matris[k][i]
                for l in range(sqrt_clear_keys):
                    birim_matris[k][l] = birim_matris[k][l] - (birim_matris[i][l] * temp)
                    inverse_matris[k][l] = inverse_matris[k][l] - (inverse_matris[i][l] * temp)
    return birim_matris
def dec_to_word():
    global birim_matris_to_fun,password,result,decrypted_list
    for x in range(len(password)):
        for y in range(len(birim_matris_to_fun)):
            for z in range(sqrt_clear_keys):
                result = result + password[x][z] * birim_matris_to_fun[y][z]
            decrypted_list.append(round(result))
            result = 0
    return decrypted_list
try:
    a = sys.argv[1]
    b = sys.argv[4]
    f=open(sys.argv[3],"r")
    input=f.read()
    f.close()
except FileNotFoundError:
    print("Input file not found error")
    sys.exit()
try:
    g=open(sys.argv[2],"r")
    key_list=g.read()
    g.close()
except FileNotFoundError:
    print("Key file not found error")
    sys.exit()
try:
    if sys.argv[3][-3:] != "txt":
        raise PermissionError
except PermissionError:
    print("The input file could not be read error")
    sys.exit()
try:
    if sys.argv[2][-3:] != "txt":
        raise PermissionError
except PermissionError:
    print("Key file could not be read error")
    sys.exit()
try:
    if len(input)<1:
        raise InputfileisemptyError
except InputfileisemptyError:
    print("Input file is empty error")
    sys.exit()
try:
    if len(sys.argv)>5 or len(sys.argv)<5:
        raise ParameterError
    if sys.argv[1] !="dec" :
        if sys.argv[1] != "enc":
            raise UndefinedParameterError
        else:
            pass
except ParameterError:
    print("Parameter number error")
    sys.exit()
except UndefinedParameterError:
    print("Undefined parameter error")
    sys.exit()
key_list=key_list.replace("\n",",")
key_list=key_list.split(",")
try:
    if len(key_list)<2:
        raise KeyfileemptyError
except KeyfileemptyError:
    print("Key file is empty error")
    sys.exit()
try:
    for i in key_list:
        i = int(i)
except ValueError:
    print("Invalid character in key file error")
    sys.exit()

sqrt_clear_keys=int(math.sqrt(len(key_list)))
letter_to_number,list2,key_nxn,encrypted_list,birim_matris_to_fun = [],[],[],[],[]
n,result=0,0
for i in range(int(len(key_list)/sqrt_clear_keys)):
    for j in range(sqrt_clear_keys):
        list2.append(int(key_list[n]))
        n+=1
    key_nxn.append(list2)
    list2=[]
if a == "enc":
    char_list,n = [],0
    for i in input:
        char_list.append(i.upper())
    for i in range(sqrt_clear_keys - (len(char_list) % sqrt_clear_keys)):
        if len(char_list) % sqrt_clear_keys == 0:
            break
        else:
            char_list.append(" ")
    try:
        for i in range(int(len(char_list) / sqrt_clear_keys)):
            for j in range(sqrt_clear_keys):
                list2.append(int(letter_number_dict[char_list[n]]))
                n += 1
            letter_to_number.append(list2)
            list2 = []
    except KeyError:
        print("Invalid character in input file error")
        sys.exit()
    n,result = 0,0
    encrypted_list=enc()
    h = open(b, "w")
    n=1
    for i in encrypted_list:
        if len(encrypted_list) == n:
            h.writelines(str(i))
            n+=1
        else:
            h.writelines(str(i) + ",")
            n+=1
if a  == "dec":
    temp, diagonal_line, n, result = 0, 0, 0, 0
    password, inverse_matris, decrypted_list = [], [], []
    input = input.split(",")
    for i in range(int(len(input) / sqrt_clear_keys)):
        for j in range(sqrt_clear_keys):
            list2.append(int(input[n]))
            n += 1
        password.append(list2)
        list2 = []
    birim_matris = deepcopy(key_nxn)
    for i in range(sqrt_clear_keys):
        for j in range(sqrt_clear_keys):
            if j != i:
                birim_matris[i][j] = 0
            else:
                birim_matris[i][j] = 1
    inverse_matris = deepcopy(key_nxn)
    birim_matris_to_fun= dec()
    decrypted_list = dec_to_word()
    h = open(b, "w")
    for item in decrypted_list:
        for key, value in letter_number_dict.items():
            if value == str(item):
                h.writelines(key)
    h.close()