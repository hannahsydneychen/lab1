strings = ['This', 'list', 'is', 'now', 'all', 'together'] 
sentence = ' '
i = 0
sentence = 'This'
for i in strings[1:]:
 	sentence = sentence+ ' ' + i
print(sentence)
print(' '.join(strings))

