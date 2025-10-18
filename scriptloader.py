import genderscript

print("GenderScript loader/interpreter")
filename = input("Type a filename: ")
scriptLoaded = True
try:
	f = open(filename)
	script = f.read()
	f.close()
except:
	scriptLoaded = False
	print("Could not open file")
if scriptLoaded == True:
	genderscript.parseGender(script)
