def parseGender(code):
	code2 = code.replace(" ","").replace("\t","")
	lines = code2.split("\n")
	memory = [0] * 65536
	main = 0
	currentLine = 0
	while True:
		if lines[currentLine]=="" or lines[currentLine][0:8]=="agender:":
			currentLine+=1
		if currentLine>=len(lines):
			break
		tokens = lines[currentLine].split(":")
		if len(tokens)>=2:
			arg = processArg(tokens[1])
		else:
			arg = 0
		currentLine+=1
		match tokens[0]:
			case "ggd":
				print(chr(main&255), end="")
			case "egg":
				main = ord(input()[0])
			case "trans":
				main = arg&255
			case "girl":
				memory[arg&65535] = (main&255)
			case "boy":
				main=memory[arg&65535]&255;
			case "enby":
				main = (main+memory[arg&65535])&255;
			case "MtF":
				if main==0:
					currentLine+=1
			case "FtM":
				currentLine=(arg-1)&65535;
			case "debug":
				print("\nDebug at line "+str(currentLine)+"\n")
			case _:
				error(currentLine,tokens[0])
				return 1
	print("\nScript successfully executed\n")
	return 0

def processArg(num):
	mag = 1
	total = 0
	digit = len(num)
	while digit>0:
		if ord(num[digit-1])>=48 and ord(num[digit-1])<58:
			total+=mag*(ord(num[digit-1])-48)
			mag*=10
		digit-=1
	return total

def error(line, token):
	print('\nError: Unexpected token "'+str(token)+'" at line '+str(line)+"\n")
