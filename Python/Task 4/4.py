def count_words(words):
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 0
            print(0, end=" ")
        else:
            word_count[word] += 1
            print(word_count[word], end=" ")

words = input().split()
count_words(words)

#one two one two three