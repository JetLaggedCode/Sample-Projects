#-- Summit

def get_score(w) :
    total_score = 0
    for letter in w :
        total_score += ord(letter) - 96
    return total_score


f = open("P:\Python27\words.txt", "r")

best_word = ""
best_score = 0

for line in f :
    word = line.strip()

    current_score = get_score(word)

    if current_score > best_score :
        best_word = word
        best_score = current_score

print best_score
print best_word
