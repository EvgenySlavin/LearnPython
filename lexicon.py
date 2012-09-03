pairs = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'go': 'verb', 'kill': 'verb', 'eat': 'verb', 'the': 'stop', 'in': 'stop', 'of': 'stop', 'bear': 'noun', 'princess': 'noun'}
		
def scan(input):
	words = input.split()
	sentence = []
	for i in words:
		if i.isdigit() == True:
			i = int(i)
			pairs.update({i: 'number'})
			word_type = pairs.get(i, 'error')
			word_pair = (word_type, i)
			sentence.append(word_pair)
		else:
			word_type = pairs.get(i, 'error')
			word_pair = (word_type, i)
			sentence.append(word_pair)
	return sentence	