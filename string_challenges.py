# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
low_a = word.lower()
count_a = low_a.count('а')
print(count_a)
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
count_vowels = 0
for char in word:
    if char in vowels:
        count_vowels += 1
print(count_vowels)
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
num_words = len(words)
print(num_words)
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
lengths = []
for word in words:
    lengths.append(len(word))
total_length = sum(lengths)
num_words_1 = len(words)
average_lenght = total_length / num_words_1
print(average_lenght)
# ???