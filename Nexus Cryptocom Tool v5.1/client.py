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






hote = input("ip?  \n> ")
port = int(input("port?  \n> "))


#hote = "localhost"
#port = 12800



#keyType = "n"
keyType = input("clé dynamique? o/n   \n> ")

if keyType == "o":
	key = key.keyDynamic()
else:
	key = key.keyGen()
	





incremType = 1
#incremType = int(input("Type d'ecrementation ? \n  1) fixe \n  2)longueure du message \n \n> "))

#incre = 0
if incremType == 1 :
	incre = int(input("incrementation? \n> "))
	
#balise à avoir
balise = str(input("balise? \n> "))

import ressources.crypt as crypt
import ressources.thread as thread

cServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cServeur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""

shootout = thread.Shootout()
shootout.start()

print("\n 'menu pour accédé au menu")



while msg_a_envoyer != b"fin":
	msg_a_envoyer = input("> ")
	#print(msg_a_envoyer)
	
	if msg_a_envoyer == "'menu":
		cr.menu()
		msg_a_envoyer = input("\n*the text under this line will be send* \n\n> ")


		
	#print(key)	
	
	

	

	

	
	
	

print("Fermeture de la connexion")
cClient.close()
cServeur.close()