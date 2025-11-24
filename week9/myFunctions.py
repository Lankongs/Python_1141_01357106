import re

def analyze(word, mostwords, mostletter):
    word = word.lower()
    letter = list(word)
    for i in letter:
        if i in mostletter:
            mostletter[i] += 1
        else:
            mostletter[i] = 1

    if word in mostwords:
        mostwords[word] += 1
    else:
        mostwords[word] = 1

def printAnswer(sorted_words, sorted_letter):
    print(f"{sorted_words[0][0]} {sorted_words[0][1]} {sorted_words[1][0]} {sorted_words[1][1]} {sorted_words[2][0]} {sorted_words[2][1]}")
    print(f"{sorted_letter[0][0]} {sorted_letter[0][1]} {sorted_letter[1][0]} {sorted_letter[1][1]} {sorted_letter[2][0]} {sorted_letter[2][1]}")

def sortAnswer(mostwords, mostletter):
    sorted_words = sorted(mostwords.items(), key=lambda item: item[1], reverse=True)
    sorted_letter = sorted(mostletter.items(), key=lambda item: item[1], reverse=True)
    return sorted_words, sorted_letter
