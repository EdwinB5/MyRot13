def myRot(text, n):
	'''
	This function receives two parameters, the text to be encrypted and 
	the rotation number of the alphabet
	'''
	upperAlph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
				'P','Q','R','S','T','U','V','W','X','Y','Z']
	lowerAlph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
				'p','q','r','s','t','u','v','w','x','y','z']

	upperRotation = upperAlph[:]
	lowerRotation = lowerAlph[:]

	textEncrypt = ''
	

	for i in range(0, n):
		upperLetter = upperRotation.pop(0)
		lowerLetter = lowerRotation.pop(0)
		upperRotation.append(upperLetter)
		lowerRotation.append(lowerLetter)

	for letter in text:
		rotationNum = 0
		for i in upperAlph:
			if letter == i:
				textEncrypt += upperRotation[rotationNum]
			rotationNum += 1

		rotationNum = 0
		for i in lowerAlph:
			if letter == i:
				textEncrypt += lowerRotation[rotationNum]
			rotationNum += 1

		if not letter in upperAlph and not letter in lowerAlph:
			textEncrypt += letter

	return textEncrypt

def myTitle(x):
		myWords = {0:'Oh no', 1:'Hello!', 2:'OMG', 3: 'It works', 4: 'Yes!', 5: 'Nope'}
		return myWords[x]