from threading import Thread
import random as rd
import __main__
import ressources.crypt as crypt
import ressources.keyPlus as keyP
import time as time



class Shootout(Thread):
	
	def __init__(self):
		Thread.__init__(self)
		
		
	def run(self):
		alph = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n',' ']
		msgInputLast = b""
		key = __main__.key
		
		while 1!=0:
			
			msgInputCheck = __main__.msg_a_envoyer
			
			if msgInputLast == msgInputCheck:
				
				word = []
				for i in range(100):
					word.append(rd.choice(alph))
					
				word = "".join(word)
				word = crypt.crypt(key, word)
				word = "".join(word)
				lenMsg = len(word)
				word = word.encode()
				__main__.cServeur.send(word)
				
				
				
			else:
				msg = crypt.crypt(key, msgInputCheck)
				msg = "".join(msg)
				balise = __main__.balise
				msg = balise + msg
				lenMsg = len(msg)
				#print(msg)
				msg = msg.encode()
				__main__.cServeur.send(msg)
					
				msgInputLast = msgInputCheck
				print(key)
				
			if __main__.incremType == 1 :
				key = keyP.keyPlus(key, __main__.incre)
			else:
				key = keyP.keyPlus(key, lenMsg)
			
			
			time.sleep(0.1)
				
				
"""
						
	lenMsg = len(msg_a_envoyer)
	msg_a_envoyer = crypt.crypt(key, msg_a_envoyer)
	
	#print(msg_a_envoyer)
	
	msg_a_envoyer = "".join(msg_a_envoyer)	
	
	#print(msg_a_envoyer)
	msg_a_envoyer = msg_a_envoyer.encode()
	cServeur.send(msg_a_envoyer)
	

	
	
	
	if incremType == 1 :
		key = keyP.keyPlus(key, incre)
	else:
		key = keyP.keyPlus(key, lenMsg)
"""