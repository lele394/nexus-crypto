import socket

import ressources.key as key
import datetime as datetime
import ressources.keyPlus as keyP

log = open("conversationLog","a")
log.write("\n \n \n \n \n \n ========= NEW CONVERSATION ========= \n \n ")

print("╔═════════════════════════════════════╗")
print("║         NEXUS  CRYPTOGRAPHY         ║")
print("║         ISN annee 2018-2019         ║")
print("║            Lycee duhamel            ║")
print("║             Leo  BECHET             ║")
print("╚═════════════════════════════════════╝")
print("\n ============== SERVER ============== \n \n")



hote = ''

port = int(input("port? \n> ")) #==========================================================

port = 12800

#keyType = 'n'

keyType = str(input("cle dynamique? o/n   \n> "))

if keyType == "o":
	key = key.keyDynamic()
else:
	key = key.keyGen()


portLog = str(port)
log.write("port : \n")
log.write( portLog)
log.write(" \n \n \n")




#incremType = int(input("Type d'ecrementation ? \n  1) fixe \n  2)longueure du message \n \n> "))

incremType = 1



if incremType == 1:
	incre = int(input("incrementation? \n> "))

import ressources.decrypt as decrypt






cPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cPrincipale.bind((hote, port))
cPrincipale.listen(5)
print("Le serveur ecoute le port {} \n \n".format(port))

#balise à avoir
balise = str(input("balise? \n> "))


cClient, infos_connexion = cPrincipale.accept()



msg_recu = b""
while msg_recu != b"fin":

	msg_recu = cClient.recv(10000000)
	
	#print(msg_recu)
	

	msg_recu = str(msg_recu).replace("b'", "")
	msg_recu = str(msg_recu).replace("'", "")
	
	#print(msg_recu)
	#=================================================================
	
	
	
	#balise
	strinMsg = [i for i in msg_recu]
	baliseDetec = []
	for i in range(len(balise)):
		baliseDetec.append(strinMsg[i])
		
	baliseDetec = "".join(baliseDetec)
	#print("balise : ",baliseDetec)
	
	if balise == baliseDetec :

		#print("bd k : ",key)
		#print(msg_recu)
		msg_recu = str(msg_recu)
		msg_recu = msg_recu.replace(balise, "")
		msg_recu = decrypt.decrypt(key, msg_recu)
		
		date = datetime.datetime.now()	
		#print(msg_recu)
		
		msg_recu = "".join(msg_recu)
		
		lenMsg = len(msg_recu)
			
		
		print("msg : ",msg_recu)
		print("----------------------")
		print("date : ",str(date))
		print("---------------------- \n \n")
		
		#log de la conversation
		
		
		log.write(msg_recu)
		log.write("\n----------------------\n")
		log.write("date : \n")
		log.write( str(date))

		log.write("\n---------------------- \n \n")	
	
	else:
		msg_recu = decrypt.decrypt(key, msg_recu)
		#print("bnd k: ",key)	
		date = datetime.datetime.now()	
		#print(msg_recu)
			
		msg_recu = "".join(msg_recu)
			
		lenMsg = len(msg_recu)
		
		
	if incremType == 1 :
		key = keyP.keyPlus(key, incre)
	else:
		key = keyP.keyPlus(key, lenMsg)
	
	
	
	
	
	
	
	

print("Fermeture de la connexion")
cClient.close()
cPrincipale.close()