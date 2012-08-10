def sixLetter():
    file = open('words')
    sLF=[]
    sL = [word for word in file if len(word)==7]
    for word in sL:
        sLF.append(word.replace('\n',''))
    return sLF
