location = 'wikiElec.ElecBs3.txt'

data = open(location, encoding='utf8', errors='ignore')
output = open('wikiElec.ElecBs3.csv', 'w', errors='ignore')

result = 0
date = ""
time = ""
candidateID = ""
candidate = ""
nominatorID = ""
nominator = ""

for line in data:
	words = line.split()
	#print(words)
	if len(words) == 0:
		continue
	if words[0] == "E":
		result = words[1]
	if words[0] == "T":
		date = words[1]
		time = words[2]
	if words[0] == "U":
		candidateID = words[1]
		candidate = words[2]
	if words[0] == "N":
		nominatorID = words[1]
		nominator = words[2]
	if words[0] == "V":
		csv = result + "|| " + date + "|| " + time + "|| " + candidateID + "|| " + candidate + "|| " + nominator + "|| " + nominatorID
		for word in words[1:]:
			csv = csv + "|| " + word
		csv = csv + "\n"
		output.write(csv)
	
	

