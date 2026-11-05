input_num = int(input())
num = input_num


def getDigs(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = int(number/10)
    return digits


result = input_num

while result>9:

    total = 1
    digits = getDigs(result)
    for dig in digits:
        if dig != 0:
            total *= dig
    result = total

print(result)
        
