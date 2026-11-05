numtest = int(input())


for case in range(numtest):
    numnotes = int(input())
    notes =[]
    s1 = False
    s2 = False
    s3 = False
    s4 = False
    for i in range(numnotes):
        inp = input()
        notes = inp.split()
        for note in notes:
            note = int(note)
            if (note<10):
                s1 = True
            elif (note < 20):
                s2 = True
            elif (note < 30):
                s3 = True
            else:
                s4 = True
    
    strings = []
    strings.append(s1)
    strings.append(s2)
    strings.append(s3)
    strings.append(s4)
    
    stringstouched = 0
    for string in strings:
        if (string):
            stringstouched+=1

print(stringstouched) 
