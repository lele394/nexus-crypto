import __main__



def menu():
	print("0) exit this menu")
	print("1) info status")
	print("2) credit")
	
	
	
	inp = int(input("> "))
	
	
	if inp == 1:
		print("key _______ : ", __main__.key)
		print("port ______ : ", __main__.port)
		print("destination : ", __main__.hote)
		
	if inp == 2:
		print("created by L.Bechet   lele394prod@gmail.com")
		print("everything done with this program is your responsability. \n we are not responsible of any trouble done \nthis program is for educationnal purposes only")
		
		