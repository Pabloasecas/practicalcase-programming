

print("1. Customer Management")
print("2. Sensor Management")
print("3. Security System Management")
print("4. Sales Management")
print("	")
print("E. End")
print("")

option=int(input("Please, insert a valid option (1-4 or E): "))

if option==1:
	
	print("1. New Customer")
	print("2. Print Customers")
	print("3. Search Customer by ID")
	print("E. End")
	option = int(input("Please, insert a valid option (1-3 or E): "))

	if option==1:
		print("You have selected option 1")
		pos=0
		a=str('')
		g=str('')
		c=str('')
		d=str('')
		e=str('')
		h=str('')
		name=input("Please introduce your name: ")
		surname=input("Please introduce your surname: ")
		ID=input("Please introduce your ID: ")
		adress=input("Please introduce your adress: ")
		town=input("Please introduce your town name: ")
		phone=input("Please introduce your phone number: ")
		a=name
		g=surname
		c=ID
		d=adress
		e=town
		h=phone
		pos=pos+1
		

		print("SUCCESS - the data of the new customer is:")
		print("Name:     ",a)
		print("Surname:  ",g)
		print("ID:       ",c)
		print("Adress:   ",d)
		print("Town:     ",e)
		print("Phone:    ",h)

		
	elif option==2:
		print("You have selected option 2")
	elif option==3:
		print("You have selected option 3")
	elif option==0:
		print("You have selected to exit from the customer management menu")
	else:
		print("Error: invalid option in customer management menu ")

elif option==2:
	
	print("1. New Sensor")
	print("2. Print Sensors")
	print("3. Search Sensors by ID")
	print("E. End")
	option = int(input("Please, insert a valid option (1-3 or E): "))

	if option==1:
		print("You have selected option 1")
	elif option==2:
		print("You have selected option 2")
	elif option==3:
		print("You have selected option 3")
	elif option==0:
		print("You have selected to exit from the sensor management menu")
	else:
		print("Error: invalid option in sensor management menu ")

elif option==3:
	print("1. New System")
	print("2. Print Systems")
	print("3. Search System by ID")
	print("E. End")
	option = input("Please, insert a valid option (1-3 or E): ")
elif option==4:
	print("1. New Sale")
	print("2. Print Sales")
	print("3. Search Sale by ID")
	print("E. End")
	option = input("Please, insert a valid option (1-3 or E): ")
elif option==0:
	print("You have selected to exit from the main menu")
else:
	print("Error: invalid option in main menu ")






