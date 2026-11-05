src = input()

op = ""
for c in src:
	match c:
		case "Á":
			op = op + "a"
		case "Ð":
			op = op + "d"
		case "É":
			op = op + "e"
		case "Í":
			op = op + "i"
		case "í":
			op = op + "i"
		case "Ó":
			op = op + "o"
		case "ó":
			op = op + "o"
		case "Ú":
			op = op + "u"
		case "á":
			op = op + "a"
		case "ö":
			op = op + "o"
		case "æ":
			op = op + "ae"
		case "ð":
			op = op +"d"
		case "þ":
			op = op + "th"
		case "ú":
			op = op + "u"		
		case "Ý":
			op = op + "y"
		case "ý":
			op = op + "y"
		case "Þ":
			op = op + "th"
		case "Æ":
			op = op + "ae"
		case "Ö":
			op = op + "o"
		case " ":
			op = op
		case "\n":
			op = op
		case _:
			op = op + c.lower()

print(op + ".is")


