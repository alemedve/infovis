from collections import Counter
import re
f = open('data/infovis-definitions.data','r')
words = re.findall(r'\w+', open('data/infovis-definitions.data').read().lower().translate(None, '.,-_'))
exclude = ['of', 'the', 'to', 'in', 'a', 'and', 'is', 'are', 'for', 'this', 'it', 'or', 'eg', 'that', 'with', 'an', 'as', 'use', 'not', 'be', 'on', 'can', 'has']
words = filter(lambda a: a not in exclude, words)
print Counter(words).most_common(15)
