from Crypto.Cipher import AES

def aes_ECB_Encrypt(pt,key):
   
    pt=padding(pt)    
    
    ctext=AES.new(key,AES.MODE_ECB)

    ct=ctext.encrypt(pt)

    return ct

def aes_ECB_Decrypt(ct,key):
    
    PT=AES.new(key,AES.MODE_ECB)

    ptext=PT.decrypt(ct)

    return ptext

def padding(mesg):
    
    pad = 16-len(mesg)%16

    padding=chr(pad)*pad
    
    print(padding)

    mesg=mesg+str(padding)

    return mesg

def Rem_Pad(mesg):

    p=bytes(mesg)[-1]

    mesg=mesg[0:-p]

    return mesg

if __name__ == '__main__':

    pt=input("Enter message: ")
    key="YELLOW SUBMARINE"

    message=aes_ECB_Encrypt(pt,key)

    print("Cipher text: ",end='')
    print(message)

    ct=message
    print()

    message=aes_ECB_Decrypt(ct,key)

    message=Rem_Pad(message)
    
    print("Plain text: ",end='')
    print(message)



