import csv
import re
with open('kurss.csv', 'r') as csv_file: #alias csv_file
	csv_reader=csv.reader(csv_file) #method .reader(), created a csv_reader variable
	next(csv_reader)
	with open('new_csv.csv', 'w', newline='') as new_file:
		csv_writer=csv.writer(new_file) #(new_file, delimiter='-')
		
		for line in csv_reader:
			csv_writer.writerow([line[1]])
			#copy the contents of the first file into the new file
	with open('new_csv.csv', 'r', newline='') as only_names:
		csv_reader2=csv.reader(only_names)	
		female=0
		male=0
		pattern=re.compile('s$|o$|kita$')
		for el in csv_reader2:
			if pattern.search(str(el[0])):
				
				male+=1
			else:
				female+=1		
		print(f'{female} females')
		print(f'{male} males')	
			
			

