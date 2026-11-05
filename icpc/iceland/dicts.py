chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def allEnglish(word):
    for char in word:
        if char not in  chars:
            return False
    return True

numDicts = int(input())

dict = {}

for i in range(numDicts):
	entry = input()
	entry_list = entry.split(' ')
	key = entry_list[0]
	value = entry_list[1]
	
	dict[key]= value

numWords = int(input())

for i in range(numWords):
    word = input()
    
    if not allEnglish(word):
        print(word)
    else:
        translated = dict.get(word)
        if translated == None:
            print("?" + word + "?")
        else:
            print(translated)
    


