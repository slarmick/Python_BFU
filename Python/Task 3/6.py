def create_abbr(words):
    abbr = ''.join(word[0].upper() for word in words.split())
    return abbr

words = input()
print(create_abbr(words))