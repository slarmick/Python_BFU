def words_frequency(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_words = sorted(word_freq, key=lambda word: (-word_freq[word], word))

    return sorted_words

text = input("Введите текст(строку): ")
sorted_words = words_frequency(text)

for word in sorted_words:
    print(word)

#abple aaple abple