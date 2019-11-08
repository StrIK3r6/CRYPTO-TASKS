import score

ctext='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

ptext=''
counter=[]
i=0
ans=[]

for word in ctext:
    for key in range(256):
        print(word)
        xor=chr(ord(word)^key)
        ptext=ptext+xor
    if(ptext.isprintable()):
     matchScore=EnglishFreqMatchOrder(ptext)
     ans.append(ptext)
     counter.append(matchscore)
     i+=1
 

j=index(max(counter))
print(ans[j])


