#Caesar Cipher Encoder by Per Esepen Schug and Julian Klotzner

alphalow = [chr(i) for i in range(ord("a"), ord("z") + 1)]  #lower case letters
alphacap = [chr(i) for i in range(ord("A"), ord("Z") + 1)]  #upper case letters

wrd = input("Please insert your word: ")                    #input box
wrdl = len(wrd)                                             #letter count
nwrd = []                                                   #empty list
shift = 3                                                   #a shift of +3 means that "A" becomes a "D"

for i in range(0, wrdl):
    if wrd[i].isupper():
        ilet = alphacap.index(wrd[i])

        if ilet <= (25 - shift):
            x = ilet + shift
        else:
            x = (ilet - 25) + (shift - 1)
        nwrd += [alphacap[x]]
    else:
        ilet = alphalow.index(wrd[i])

        if ilet <= (25 - shift):
            x = ilet + shift
        else:
            x = (ilet - 25) + (shift - 1)
        nwrd += [alphalow[x]]


ewrd = "".join(nwrd)                                        #changing list into string
print(ewrd)
