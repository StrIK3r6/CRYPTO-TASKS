from Crypto.Util import Counter
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from base64 import b64decode


def ctr_implement(ct,key):
	
	plaintext=''
	cipher_blocks=[ct[i*16:(i+1)*16] for i in range(0,4)]
	for index in range(len(cipher_blocks)):
		
		iv=chr(0)*8+chr(index)+chr(0)*7
		Encrypted_iv=iv_encrypt(key,iv)
		Encrypted_iv=Encrypted_iv[:len(cipher_blocks[index])]
		
		pt=''
		for iv_byte,ct_byte in zip(Encrypted_iv,cipher_blocks[index]):

			pt+=chr(ord(iv_byte)^ord(ct_byte))
		
		plaintext+=pt

	return plaintext

def iv_encrypt(key,iv):

	cipher=AES.new(key,AES.MODE_ECB)
	ct=cipher.encrypt(iv)
	return ct

if __name__ == '__main__':

	cipher=''
	ciphertext="L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
	ciphertext=b64decode(ciphertext)
	print ciphertext
		
	key="YELLOW SUBMARINE"
	
	plaintext=ctr_implement(ciphertext,key)
	print plaintext
	ctext=ctr_implement(plaintext,key)
	print ctext
