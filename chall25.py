from CTRMODE import *
from Crypto.Cipher import AES
from base64 import b64decode
from os import urandom
from tqdm import tqdm

def edit(ciphertext,offset,newtext,key):
    plaintext = ctr_implement(ciphertext,key)
    new_ciphertext = ctr_implement(plaintext[:offset]+newtext+plaintext[offset:],key)
    return new_ciphertext

if __name__ == '__main__':
    
    aes = AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
    ct = open('chall25.txt').read().strip()
    ct = b64decode(ct) 
    plaintext = aes.decrypt(ct) 

    key = urandom(16)
    ciphertext = ctr_implement(plaintext,key)
   
    flag = ''
    print "Extracting message......."
    for i in tqdm(range(len(ciphertext))):
        cipher_byte = ciphertext[i]
       
        for j in range(256):
            flag_byte = edit(ciphertext,i,chr(j),key)[i]
            if flag_byte == cipher_byte:
                flag += chr(j)
                # print("flag {}".format(flag))

    print("Extracted message is\n\n{}".format(flag))
