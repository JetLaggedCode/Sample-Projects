#-- Palindromes

def reverse_word(word) :
    palindrome = True
    for i in range(len(word) ) :
        if word[i] != word[len(word) - i - 1] :
            palindrome = False

    return palindrome


f = open("P:\Python27\words.txt", "r")

best_word = ""
best_score = 0

for line in f :
    word = line.strip()

    if reverse_word(word) :
        print word
