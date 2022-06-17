from collections import deque
import re


def check_if_found_word(found_words, searched_words):
    for index, word_as_list in enumerate(found_words):
        word = ''.join(word_as_list)
        if word == searched_words[index]:
            return True, word
    return False, None


vowels = deque(input().split())
consonants = input().split()
searched_words = ('rose', 'tulip', 'lotus', 'daffodil')
found_words = []
for word in searched_words:
    found_words.append(['-'] * len(word))

is_found_word = False
found_word = None
while vowels and consonants:
    current_chars = (vowels.popleft(), consonants.pop())
    for ch in current_chars:
        for index, word in enumerate(searched_words):
            if ch in word:
                for i in re.finditer(ch, word):
                    found_words[index][i.start()] = ch
                is_found_word, found_word = check_if_found_word(found_words, searched_words)
                if is_found_word:
                    break
    if is_found_word:
        break

if is_found_word:
    print(f"Word found: {found_word}")
else:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
