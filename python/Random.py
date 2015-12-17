import random

def generateWord(lstWords):
	#Get a random number fom 0 to lst lenght-1
	rndIndx = random.randrange(0,(len(lstWords)-1),1)
	return lstWords[rndIndx].lower()#Get word and convert to lower case
      
def checkLetter(word):
	#Replace each lettler with a underscore
	word = ["_" for s in word]
	return " ".join(word)#Return the replaced word with underscore but repared with a space	

lstWords = []#Declare an empty list
fs = open('vocabulary.txt','wt')#Open a new file stream
for i in range(3):
	while True:
		word = raw_input("Type a word :")
		if not word.isalpha():
			print("Numbers and special chars are not allowed \n Try again")
		else: 
			lstWords.append(word)#Add word into the list
			fs.write(word+"\n")#Write word into the file
			break
			
fs.close()#Close the file stream


rndWord = generateWord(lstWords)
print("Random word:%s"%"_".join(rndWord))

print ("Underscrore word:\n%s"%checkLetter(rndWord))

