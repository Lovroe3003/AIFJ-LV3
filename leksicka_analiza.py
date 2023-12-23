import re
from operators import is_operator
from keywords import is_keyword
from separator import isSeparator
from comment import isComment
from constant import isConstant
from pathlib import Path
from collections import Counter

def analyze_keyword(word):
    print("('",word,"', ključna riječ)")
    #Ako procita var ili fun postavlja zastavicu last_word na True da bi se sljedeca rijec mogla spremiti kao identifikator
    if word == "var" or word == "fun" or word == "const":
        return True
    return False

filepath = Path(__file__).parent / "primjerKoda.txt"
file = open(filepath, "r")

lines=file.readlines()

keyword = []
identifier = []
operator = []
separator = []
comments = []
constants = []

if len(lines) <= 0:
    print ("Prazan fajl!")
    quit(0)

line_number = 1

for line in lines:
    print("---- Linija: ", line_number, "----")
    line_number += 1
    last_word = False
    last_word_const = False
    #Regularni izraz koristen da bi se separatori i operatori odvojili razmacima
    words = re.sub(r"(\(|\)|;|\+|\-|\=|\#)", r' \1 ', str(line))
    #Funkcija regularnog izraza koja razdvaja sve između razmaka i stavlja u niz
    words = words.split()

    if isComment(words[0]):
        comments.append(words[0])
        print("('",words[0],"', komentar), (",' '.join(words[1:]),")")
        continue

    #Prolazi kroz svaku rijec i analizira
    for word in words:
        #Analizira je li riječ vec definiran keyword
        if is_keyword(word):
            keyword.append(word)
            last_word = analyze_keyword(word)
            continue 

        if is_operator(word):
            operator.append(word)
            print("('",word,"', operator)")
            continue

        if isSeparator(word):
            separator.append(word)
            print("('",word,"', separator)")
            continue
            
        if isConstant(word):
            keyword.append(word)
            print("('",word,"', ključna riječ)")
            last_word_const = True
            continue

        if last_word_const:
            constants.append(word)
            print("('",word,"', konstanta)")
            last_word_const = False
            continue

        if last_word:
            #Dodaje trenutnu rijec u listu identifikatora ako je zadnja bila var ili fun
            identifier.append(word)
            print("('",word,"', identifikator)")
            last_word = False
            continue

        if word in identifier:
            print("('",word,"', identifikator)")
            continue

        if not is_keyword(word) or not is_operator(word) or not isSeparator(word):
            print("('",word,"', vrijednost)")

print("Ključne riječi: ", len(keyword), str(Counter(keyword))[8:-1])
print("Identifikatori: ", len(identifier), str(Counter(identifier))[8:-1])
print("Separatori: ", len(separator), str(Counter(separator))[8:-1])
print("Operatori: ", len(operator), str(Counter(operator))[8:-1])
print("Komentari: ", len(comments), str(Counter(comments))[8:-1])
print("Konstante: ", len(constants), str(Counter(constants))[8:-1])