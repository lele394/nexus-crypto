import ressources.matrix as m
import numpy as np
import ressources.plan as pl
import ressources.axis as axis



def crypt(key, messageListe):
	lengthMsg = len(messageListe)
	crypted = []
	for i in range(lengthMsg) :
		plan = pl.plan(key, i)
		coordo = np.where(plan==ord(messageListe[i])) 
		coordo = str(coordo).replace("], dtype=int32))", "")
		coordo = str(coordo).replace("(array([", "")
		#print(coordo)
		coordo = [i for i in coordo]
		x = coordo[0]
		y = coordo[-1]
		#print(x,"    ",y)
		
		x = axis.xShift(x)
		y = axis.yShift(y)
		#print(x,"    ",y)
		y = str(y)
		x = str(x)
		crypted.append(x)
		crypted.append(y)

	return crypted