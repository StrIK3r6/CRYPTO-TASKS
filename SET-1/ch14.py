import score

f=open("testfile1.txt","r")

ptext=''
counter=[]
i=0
ans=[]

for i in range(60):

    ctext=f.readline()

    for word in ctext:
        for key in range(256):

             print(word)
             xor=chr(ord(word)^key)
             ptext=ptext+xor

        if(ptext.isprintable()):
             matchScore=EnglishFreqMatchOrder(ptext)
             ans.append(ptext)
             counter.append(matchscore)
       
print(ans) 
print(counter)
j=index(max(counter))
print(ans[j])
