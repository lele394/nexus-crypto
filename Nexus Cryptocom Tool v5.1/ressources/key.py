import datetime as dt




def keyGen():
  inpKey=input("\n Veuillez entrez le clé : \n \n      ") #entrée de la clé
  key = []
  cKey= 0
  inpKey = [i for i in inpKey ]
  k=int(len(inpKey)/2)

  for i in range(k) :
    keyNum = []
    keyNum.append(inpKey[cKey])
    cKey = cKey+1
    keyNum.append(inpKey[cKey])
    cKey = cKey+1
    keyJoin = "".join(keyNum)
    key.append(keyJoin)
    keya = [int(i) for i in key]
  return keya
  
  
  
  
  
def keyDynamic():
	key = []
	now = dt.datetime.now()
	key.append((now.year)%12 +11)
	key.append((now.month)%12 +11)
	key.append((now.day)%12 +11)
	key.append((now.hour)%12 +11)
	key.append((now.minute)%12 +11)
	
	
	return key
	