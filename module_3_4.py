def single_root_words(root_word, *other_words):
    root_word.lower()
    other_words = [s.lower() for s in other_words]

    same_words = []
    for _ in other_words:
        if other_words.count(root_word):
            same_words += root_word

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
