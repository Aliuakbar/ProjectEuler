from string import ascii_lowercase

triangles = [n*(n+1)/2 for n in range(1, 50)]

vals = dict(zip(list(ascii_lowercase), range(1, 27)))
vals['"'] = 0

def word_value(word):
	value = 0
	for char in word.lower():
		value += vals[char]
	return value

def solve():
	counter = 0
	with open("words.txt", "r") as text:
		words = text.read().split(",")
		print(len(words))
		for word in words:
			if word_value(word) in triangles:
				print(word, word_value(word))
				counter += 1
	return counter

print(solve())
