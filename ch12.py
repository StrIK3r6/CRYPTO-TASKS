import base64

def main():
    base16='49276d206b69c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    base16=base16.decode('hex')

    print(base16)

    b64=base64.b64encode(base16)

    print(b64)


main()
      

