from Crypto.Cipher import AES
import base64

def padding(mesg):

    pad = 16-len(mesg)%16
    padding=pad*chr(pad)
    mesg=mesg+str(padding)
    return mesg

def aes_ECB_Encrypt(inp):
    
    secret=str(base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZ    yBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"))
    pt=inp+secret
    pt=padding(pt)
    ctext=AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
    ct=ctext.encrypt(pt)
    return ct

def Repeat_check(Rand_bytes):

    inp=Rand_bytes
    repeating_block="aaaaaaaaaaaaaaaa"
    for i in range(32,48):
        inp+='a'*i
        ct=aes_ECB_Encrypt(inp)
        ct_blocks=[ct[j*16:(j+1)*16] for j in range(0,len(ct)//16)]
        if (repeating_block in ct_blocks):
            new_ct=ct_blocks[ct_blocks.index(rep_block)+2:]
            print(new_ct)
            return new_ct
            break
    
def exploit(Rand_bytes):
    
    ct=Repeat_check(Rand_bytes)
    flag=""
    for i in range(1,20):
        
        for k in range(15,-1,-1):
            inp=k*'a'
            control_block=aes_ECB_Encrypt(inp)
            
            for char in range(256):
                flag_block=aes_ECB_Encrypt(inp+flag+chr(char))

                if (flag_block[:i*16]==control_block[:i*16]):
                    flag+=chr(char)
                    break

    return flag       

if __name__ == '__main__':

    Rand_bytes="stimulus and response"
    flag=exploit(Rand_bytes)
    print("Decoded message is: ")
    print(flag)


