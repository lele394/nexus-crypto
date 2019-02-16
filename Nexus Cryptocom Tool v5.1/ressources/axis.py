import random as rd
import math as m

seed = float(input("cle de melange des axes? ( 0 < x < 1 )\n \n "))
seed = 0.1
seed = seed/10000


rd.seed(int(1/seed)*m.cos(1/seed))

axex = [0,1,2,3,4,5]

rd.shuffle(axex)
#print("axex     ",axex)


a1 = axex[0]
a2 = axex[1]
a3 = axex[2]
a4 = axex[3]
a5 = axex[4]
a6 = axex[5]

axey = [0,1,2,3,4,5]

rd.shuffle(axey)
#print("axey     ",axey)



o1 = axey[0]
o2 = axey[1]
o3 = axey[2]
o4 = axey[3]
o5 = axey[4]
o6 = axey[5]

naxex = ['0','1','2','3','4','5']
naxey = ['0','1','2','3','4','5']

def xShift(x):
	#x = int(x)
	x = naxex.index(x)
	x = axex[x]
	x = int(x)
	return x

	
def yShift(y):
	#x = int(y)
	y = naxey.index(y)
	y = axey[y]
	y = int(y)
	return y
	
def xUnshift(x):
	#x = int(x)
	x = axex.index(x)
	x = naxex[x]
	x = int(x)
	return x

def yUnshift(y):
	#x = int(y)
	y = axey.index(y)
	y = naxey[y]
	y = int(y)
	return y











