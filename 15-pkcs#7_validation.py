#Function to check pkcs#7 padding on an aes encrypted message

check_pad(mesg):
	try:j
		mesg=bytes(mesg)
		pad_char=bytes(mesg)[-1]
		for i in range(len(mesg)-1,len(mesg)-(pad_char+1),-1):
			if mesg[i]!=pad_char:
				raise

		mesg=''.join( char for char in mesg if char not in pad_char)
		print(mesg)

	except:
		print("INVALID PADDING!!")


if __name__ == '__main__':

	pt=input("Enter padded message: ")
    check_pad(message)
