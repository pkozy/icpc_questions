

def roundUp(n):
    n = str(n)
    first = int(str(n)[0])
    first += 1
    first *= 10**(len(n)-1)
    return first

def roundDown(n):
    n = str(n)
    first = int(str(n)[0])
    first *= 10**(len(n)-1)
    return first

num_str = input()
num = int(num_str)

if len(num_str) == 1:
    print(num)
else:
    second = int(num_str[1])

    if second >=5:
        print(roundUp(num))
    else:
        print(roundDown(num))

