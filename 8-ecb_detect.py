import base64oracle

def ecb_Detect(ctext):

	if(len(ctext)%16!=0):
		print('',end='')

	else:
		print()
		no_of_blocks=len(ctext)//16

	Blocks=[ctext[i*16:(i+1)*16] for i in range(no_of_blocks)]

	if len(check_Blocks(Blocks))!=no_of_blocks:
		return True

	else:
		return False

def check_Blocks():
	
	block = [] 
    for i in Blocks: 
    	if i not in blockck: 
        	temp.append(i)
    return block
  
if __name__ == '__main__':
	
	foo=open('ecbDetect.txt','r')
	c_texts = [base64.b64decode(foo.readline()) for line in foo]
	ecb_encrypted_text=[ctext for ctext in c_texts if ecb_Detect(ctext)]
	print(ecb_encrypted_text)
