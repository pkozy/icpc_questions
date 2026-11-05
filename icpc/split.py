firstLine = input()
secondLine = input()

firstWord = firstLine.split("|")[0]
secondWord = firstLine.split("|")[1]

firstWord += secondLine.split("|")[0]
secondWord += secondLine.split("|")[1]

print(firstWord + " " + secondWord)

