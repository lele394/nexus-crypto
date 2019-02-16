import ressources.matrix as m
import numpy as np
import ressources.plan as pl
import ressources.axis as axis


def decrypt(key, messageListe):
	lengthMsg = len(messageListe)
	decrypt = []
	c=0
	for i in range(int(lengthMsg/2)) :
		plan = pl.plan(key, i)
    #
		x = int(messageListe[c])
		y = int(messageListe[c+1])
		#print(x,"    ",y)
		
		x = axis.xUnshift(x)
		y = axis.yUnshift(y)
		c=c+2
		#print(x,"    ",y)
		decrypt.append(chr(plan[x][y]))
    
	return decrypt


