''' 
Author: Brooke Boatman
Date: March 2016
Python cleaner file to clear up Java scraping data dumps
'''

list = []
with open("holdFile.txt", "r") as hold:
	for line in hold.readlines():
		clean = line[1:-2]
		tupleAr = clean.split(", ")
		if int(tupleAr[1]) > 3:
			list.append(clean)

with open("holdFile.txt", "w") as hold:
	for item in list:
		hold.write(item + "\n")