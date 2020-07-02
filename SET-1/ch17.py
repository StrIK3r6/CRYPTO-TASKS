from Crypto.Cipher import AES

def aes_ECB_Decrypt(ctext):

    ctext = ctext.decode('base64')
    
    key="YELLOW SUBMARINE"

    ptext = AES.new(KEY, AES.MODE_ECB)

    return ptext.decrypt(ctext)

if __name__ == '__main__':

    foo = open("aes_ecb.txt","r")
    
    ctext = foo.read()
    
    ptext = aes_ECB_Decrypt(ctext)

    foo.close()

    print(ptext)
    



