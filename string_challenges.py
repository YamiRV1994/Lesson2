word = 'Архангельск'
last_letter = word[-1]
print(last_letter)
count_a = word.lower().count('а')
print(count_a)
glass = 'аеёиоуыэюя'
count_glass = sum(1 for letter in word.lower() if letter in glass)
print(count_glass)
sentence = 'Мы приехали в гости'
words_count = len(sentence.split())
print(words_count)
first_letters = [word[0] for word in sentence.split()]
for letter in first_letters:
    print(letter)
words = sentence.split()
long = sum(len(word) for word in words) / len(words)
print(long)
