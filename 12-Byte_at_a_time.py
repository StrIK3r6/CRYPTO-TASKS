from Crypto.Cipher import AES
import base64

def secretLen(secret):

    prev_Value=16
    for i in range(0,16):

        final_text=i*'a'+secret
        final_text=padding(final_text)
    	Block_no=len(final_text)/16
    	if Block_no>prev_Value:
    	    secret_len=16-i

    	prev_Value=Block_no

    return(secret_len)

def exploit(secret):

    secret_len=secretLen(secret)
    flag=''
    for i in range(15,15-secret_len,-1):
    	f_block=i*'a'+flag
    	f_block=aes_ECB_Encrypt(padding(f_block))
    	for char in range(256):
    		b_block=i*'a'+flag+chr(char)
    		b_block=aes_ECB_Encrypt(padding(b_block))
    		if b_block==f_block:
    			flag+=char 

    print(flag) 
    

def padding(mesg):

    pad = 16-len(mesg)%16
    padding=pad*chr(pad)
    mesg=mesg+str(padding)
    return mesg

def aes_ECB_Encrypt(final_text,key):

    pt=padding(pt)
    ctext=AES.new(key,AES.MODE_ECB)
    ct=ctext.encrypt(pt)
    return ct

if __name__ == '__main__':

    key="YELLOW SUBMARINE"
    secret=str(base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"))
