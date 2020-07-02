ptext=b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

ctext=b''
keyList=b"ICE"
count=0

for char in ptext:
    
    ctext+=bytes([char^keyList[count]])
    
    count+=1
    if count==3:
        count=0

print(ctext.hex())
    
