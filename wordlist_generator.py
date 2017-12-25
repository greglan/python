from itertools import combinations

PREFIX = ''
SUFFIX = ''

words = []
f_words = open('words.txt', 'r')
for line in f_words:
    words.append(line.strip())
f_words.close()

word_list = [PREFIX + ''.join(w) + SUFFIX for w in combinations(words)]

f_output = open('wordlist.txt', 'w')
for word in word_list:
    f_output.write(word+'\n')
f_output.close()
