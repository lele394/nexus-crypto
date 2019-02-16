import socket
import ressources.key as key
import ressources.keyPlus as keyP
import random as rd
import ressources.credit as cr

print("╔═════════════════════════════════════╗")
print("║         NEXUS  CRYPTOGRAPHY         ║")
print("║         ISN annee 2018-2019         ║")
print("║            Lycee duhamel            ║")
print("║             Leo  BECHET             ║")
print("╚═════════════════════════════════════╝")
print("\n ============== CLIENT ============== \n \n")






hote = input("ip?  ")
port = int(input("port? "))

"""
hote = "localhost"
port = 12800
"""


#keyType = "o"
keyType = input("clé dynamique? o/n   ")

if keyType == "o":
	key = key.keyDynamic()
else:
	key = key.keyGen()
	





#incremType = 2
incremType = int(input("Type d'ecrementation ? \n  1) fixe \n  2)longueure du message \n \n  "))

incre = 0
if incremType == 1 :
	incre = int(input("incrementation? "))

import ressources.crypt as crypt


cServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cServeur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

print("\n 'menu pour accédé au menu")


msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
	msg_a_envoyer = input("> ")
	print(msg_a_envoyer)
	if msg_a_envoyer == "'menu":
		cr.menu()
		msg_a_envoyer = input("\n*the text under this line will be send* \n\n> ")
		
		
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
		
	#print(key)	
	
	

	

	

	
	
	

print("Fermeture de la connexion")
cClient.close()
cServeur.close()