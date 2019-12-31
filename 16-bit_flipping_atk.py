from Crypto.Cipher import AES

def aes_CBC_Encrypt(pt):

		pt="comment1=cooking%20MCs;userdata="+pt
		pt+=";comment2=%20like%20a%20pound%20of%20bacon"
		pt=pt.replace(';','?').replace('=','?')
	    	pt=padding(pt)	   
        	ctext=AES.new("ALL HAIL CRYPTOO",AES.MODE_CBC,"YELLOW SUBMARINE")
	    	ct=ctext.encrypt(pt)
	    	return ct

def padding(pt):
		
		padlen=16-(len(pt)%16)
	    	padbytes=padlen*chr(padlen)
	    	pt+=padbytes
	    	return pt

def aes_CBC_Decrypt(ct):

		ptext=AES.new("ALL HAIL CRYPTOO",AES.MODE_CBC,"YELLOW SUBMARINE")
		message=ptext.decrypt(ct)
		if ";admin=true;" in message:
			print "You are admin now"
		else:
			print "You must be logged in as admin to get access"

#bit flipping attack execution function!

def exploit(ct):

		Cipher_blocks=[]
		for i in range(len(ct)/16):
			Cipher_blocks.append(ct[i*16:(i+1)*16])
		block1=list(Cipher_blocks[1])
		block1[0]=chr(ord(block1[0])^ord(';')^ord('?'))
		block1[6]=chr(ord(block1[6])^ord('=')^ord('?'))
		block1[11]=chr(ord(block1[11])^ord(';')^ord('?'))
		Cipher_blocks[1]=''.join(block1)
		ct=''.join(Cipher_blocks)
		return ct

if __name__ == '__main__':

		payload=';admin=true;'
		final_text=exploit(aes_CBC_Encrypt(payload))
		aes_CBC_Decrypt(final_text)


