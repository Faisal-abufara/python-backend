words = ["Faisal", "Hamza"]

ascii_dict = {
    word: {char: ord(char) for char in set(word)}
    for word in words
}

print(ascii_dict)