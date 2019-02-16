def keyPlus(key, increm):
	for i in range(len(key)):
		key[i] = (key[i] + increm) % 12 + 11
	return key
	
	
	
def keyPlusLenMsg(key, increm):
	for i in range(len(key)):
		key[i] = (key[i] + increm) % 12 + 11
	return key