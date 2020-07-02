englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}


ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#returns the no of times a letter is repested in the ctext in a dictionary
def get_letterCount(ctext):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H':     0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,      'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in ctext.upper():
        if letter in LETTERS:
            letterCount[letter]+=1

    return(letterCount)

def get0index(x):
    return(x[0])


#returns a string containing alphabets in order of most repeating character in ctext 
def get_frequencyOrder(ctext):

    lettertoFreq=get_letterCount(ctext)

    freqtoletter={}
    for letter in LETTERS:
        if lettertoFreq[letter] not in freqtoltter:
            freqtoletter[lettertoFreq[letter]]=[letter]
        else:
            freqtoletter[lettertoFreq[letter]].append[letter]
                                                                                                                              1,5           Top

  #extracting the ist of elements from the dictionary and reversing it in the order of 'ETAOIN"
    for freq in freqtoletter:
        freqtoletter[freq].sort(key=ETAOIN.find, reverse=True)
    #converting the list of letters obtained into a string
        frqtoletter[freq]=''.join(freqtoletter[freq])


    freqpairs=list(freqtoletter.items())
    freqpairs.sort(key=get0index,reverse=True)

    final=[]
    for freqpair in freqpairs:
        final.append(freqpair[1])

    return(''.join(final))

#detrmines how many of the 6 most freq letter and least frequent letters are present in the six most occurring and 6 least occurring alhpabetsin english language

def EnglishFreqMatchOrder(ctext):

    final=get_frequncyOrder(ctext)


    matchScore=0

    for match in ETAOIN[:6]:
        if match in final[:6]:
            matchScore+=1

    for match1 in ETAOIN[6:]:
        if match1 in final[-6:]:
            matchScore+=1

    return(matchSCore)
                                                                                                                              64,5          84%


