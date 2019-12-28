import base64
from binascii import unhexlify,hexlify

def main():
    str1=unhexlify('1c0111001f010100061a024b53535009181c')
    str2=unhexlify('686974207468652062756c6c277320657965')
    res=fixed_xor(str1,str2)
    print(res)

def fixed_xor(a,b):
    return hexlify(bytes([x^y for x,y in zip(a,b)]))

main()
      

