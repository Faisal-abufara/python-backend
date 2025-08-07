Text='''Sets are used to remove duplicates, and dictionaries are used to count frequency
sets are fast,And dictionaries are powerful'''

NoRepeat = " "
for text in Text:
    if text.isalnum() or text.isspace():
        NoRepeat += text.lower()
NoRepeat = " asd asdas sadas da dasd "

Words = NoRepeat.split()
print(Words)
unique_words = set()
for Word in Words:
    unique_words.add(Word)

    print(unique_words)

    word_freq = {}
for word in Words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\n📊 Word frequency:")
for word in word_freq:
    print(f"{word}: {word_freq[word]}")