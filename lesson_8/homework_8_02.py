last_words = input('Введите слова: ')

# reverse_words_new = reverse_words[::-1]
# print(reverse_words)
def polindrom(str):
    new_list = str.split()
    reverse_words = [i[::-1] for i in new_list]
    for i in range(len(new_list)):
        if reverse_words[i] == new_list[i]:
            print(reverse_words[i])



polindrom(last_words)
