fp = open('words_alpha.txt','r')
lines = fp.read()

if('TEPHI' in lines):
	print("Found")
else:
	print("No")