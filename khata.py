print("__________________________________________________")
print("\n\033[07mkhata by Sukant \033[27m | \033[07msukant929@protonmail.com\033[27m")
print("\033[07m\033[1;31mWordlist & Mobile Number Generator...\033[1;m \033[27m\n")
print("Example:")
print("\nEnter Name: \033[1;31msukant\033[1;m     |leave empty if you want to generate only numbers.")
print("Number Start from: \033[1;31m0\033[1;m   |you must enter a value.")	
print("Number Ends at: \033[1;31m5\033[1;m      |you must enter a value.")
print("Save as: \033[1;31msukant.txt\033[1;m    |leave empty if you don't want to save output.")
print("\n\033[1;31msukant0\nsukant1\nsukant2\nsukant3\nsukant4\nsukant5\033[1;m\nsaved as sukant.txt")
print("__________________________________________________")
name = raw_input('\nEnter Name: ')
min_n = ''
max_n = ''
while min_n == '':
	min_n = raw_input('Number Start from: ') 
while max_n == '':
	max_n = raw_input('Number End at: ') 
min_n = int(min_n)  
max_n = int(max_n)  
max_n = max_n + 1
file_name = raw_input('Save as: ')
if file_name == '':
	while (min_n < max_n):
			i = name+str(min_n)
			print (i)
			min_n = min_n + 1
else:
	with open(file_name,"w") as f:
		while (min_n < max_n):
			i = name+str(min_n)
			print (i)
			f.write(i + "\n")
			min_n = min_n + 1
	print ("Saved as '" + file_name + "'")
