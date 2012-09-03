pairs = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'go': 'verb', 'kill': 'verb', 'eat': 'verb', 'the': 'stop', 'in': 'stop', 'of': 'stop', 'bear': 'noun', 'princess': 'noun'}
		
def scan(input):
	words = input.split()
	sentence = []
	for i in words:
		try:
			i = int(i)
			pairs.update({i: 'number'})
			return i
		except ValueError:
			return None
		word_type = pairs.get(i, 'error')
		word_pair = (word_type, i)
		sentence.append(word_pair)
	return sentence	