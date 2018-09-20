import pandas as pd

location = 'data/wikiElec.txt'
output = 'data/wikiElec.csv'

data = open(location)

columns = ['result',
 'nomination_date',
 'nomination_time',
 'candidate_id',
 'candidate_user',
 'nominator_id',
 'nominator_user',
 'vote',
 'voter_id',
 'voter_user',
 'vote_date',
 'vote_time']

row = {}
elec = pd.DataFrame(columns=columns)

for line in data:
	words = line.split()
	if len(words) == 0:
		continue
        if words[0] == '#':
                continue
	if words[0] == 'E':
                #print(words)
                row['result'] = words[1]
	if words[0] == 'T':
                #print(words)
                row['nomination_date'] = words[1]
                row['nomination_time'] = words[2]
	if words[0] == 'U':
                #print(words)
		row['candidate_id'] = words[1]
		row['candidate_user'] = words[2]
	if words[0] == 'N':
                #print(words)
		row['nominator_id'] = words[1]
		row['nominator_user'] = words[2]
	if words[0] == 'V':
                row['vote'] = words[1]
                row['voter_id'] = words[2]
                row['vote_date'] = words[3]
                row['vote_time'] = words[4]
                row['voter_user'] = words[5]
                
                elec = elec.append([row])

elec.to_csv(output,index=False)
