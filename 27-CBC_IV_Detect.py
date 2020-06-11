from Crypto.Cipher import AES
from os import urandom

iv = urandom(16)
key = urandom(16)

def cbc_encrypt(key,iv,message):

	ct = AES.new(key,AES.MODE_CBC,iv)
	return ct.encrypt(padding(message))

def cbc_decrypt(key,iv,ciphertext):

	#ciphertext = ciphertext.decode('hex')
	pt = AES.new(key,AES.MODE_CBC,iv)
	return pt.decrypt(ciphertext)

def padding(message):

	pad_bytes = 16 - len(message)%16 
	message = message + pad_bytes*(str(pad_bytes))
	print(message)
	return message

def exploit(key,iv):

	message = "a"*48
	ctext = cbc_encrypt(key,iv,message)

	print("[.]Cipherteext: {}".format(ctext))

	exploit_text = ctext[:16] + "\x00"*16 + ctext[:16]
	obtained_text = cbc_decrypt(key,iv,exploit_text)
	plaintext_1,plaintext_2 = obtained_text[:16], obtained_text[32:]

	obtained_key=''
	for p1,p2 in zip(plaintext_1,plaintext_2):
		obtained_key+= chr((ord(p1)^ord(p2)))	

	print(obtained_key)
	print(key)

if __name__ == '__main__':
	exploit(key,iv)
