from CTRMODE import *

def encode_cookie(pt):
	
	pt = "comment1=cooking%20MCs;userdata=" + pt + ";comment2=%20like%20a%20pound%20of%20bacon"
	pt = pt.replace('=','?')
	
	return ctr_implement(pt)
 
def admin_check(encrypted_cookie):

	plaintext = ctr_implement(encrypted_cookie)
	if "admin=true" in plaintext:
		print("Logged in as admin!! Here is the flag: crypto{Ju57_Fl1p_Th3_B1t5!}")
	else:
		print("You are not admin!!! No flag for you!!!")

if __name__ == '__main__':
	
	encrypted_cookie = encode_cookie("admin=true")

	encrypted_cookie = encrypted_cookie[:37] + chr(ord(encrypted_cookie[37]) ^ ord("?") ^ ord("=")) + encrypted_cookie[38:]

	admin_check(encrypted_cookie)