from Crypto.Cipher import aes
import os
import random

def encryption_oracle(mode,pt):

	key=os.urandom(128)
	rand_bytes=random.randint(5,10)*A
	pt=rand_bytes+pt+rand_bytes

	def aes_ECB_Encrypt(pt,key):
   
    		ctext_ecb=AES.new(key,AES.MODE_ECB)
    		ct=ctext_ecb.encrypt(padding(pt))
    		return ct

	def padding(pt):
    
    		pad = 16-len(pt)%16
    		padding=chr(pt)*pad    
    		print(padding)
    		mesg=pt+str(padding)
    		return mesg
	
	def aes_CBC_Encrypt(pt,key):

		iv=16*'\x00'
		while(len(pt)%16!=0):
			pt+='A'
		ctext_cbc=AES.new(key,AES.MODE_CBC,iv)
		ct=ctext_cbc.encrypt(pt)
		return ct

	if mode=='ecb':
		Cipher_text=aes_ECB_Encrypt(pt,key)

	else:
		Cipher_text=aes_CBC_Encrypt(pt,key)

	return Cipher_text


def ecb_cbc_Detect(ctext):

	if(len(ctext)%16!=0):
		print('',end='')

	else:
		print()
		no_of_blocks=len(ctext)//16

	Blocks=[ctext[i*16:(i+1)*16] for i in range(no_of_blocks)]

	if len(check_Blocks(Blocks))!=no_of_blocks:
		return "ECB"

	else:
		return "CBC"


if __name__ == '__main__':
	
	message='HELLO'
	choice=random.randint(1,2)
	if choice==1:
		mode='ecb'
	else:
		mode='cbc'
	Cipher_text=encryption_oracle(mode,message)
	aes_mode=ecb_cbc_Detect(Cipher_text)
	print(aes_mode)

