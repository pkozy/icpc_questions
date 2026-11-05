
def isLiked(digitlist): 
    for i in range(len(digitlist)-1):
        if digitlist[i+1] != digitlist[i]-1:
            return False
    return True

def toList(num):
    digitlist = []
    
    while(num > 1):
        digitlist.append(int(num%10))
        num = num/10
        
    return digitlist
    
cases = int(input())


for i in range(cases):
    
    numstr = input()
    num = int(numstr)
    digitlist = toList(num)
    
    while(isLiked(digitlist) == False):
        num+=1
        digitlist = toList(num)
    
    print(num)  
    
