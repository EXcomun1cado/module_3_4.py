def single_root_words(root_word, *other_words):
    word = root_word.lower()
    other = [s.lower() for s in other_words]

    same_words = []
    for words in other:
        if word in words or words in word:
            same_words.append(words)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
