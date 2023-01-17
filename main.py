with open("books/frankenstein.txt") as f:
    file_contents = f.read()
#print(file_contents)
#words = len(file_contents.split())
words = file_contents.split()
word = file_contents
print("--- Begin report of books/frankenstein.txt ---")
listedtxt= word.lower()
sortedtxt = list(listedtxt)
txt = sorted(sortedtxt)
#for letter in txt:
print("The 'e' character was found ",txt.count('e'), " times")
print("The 't' character was found ",txt.count('t'), " times")
print("The 'a' character was found ",txt.count('a'), " times")
print("The 'o' character was found ",txt.count('o'), " times")
print("The 'i' character was found ",txt.count('i'), " times")
print("The 'n' character was found ",txt.count('n'), " times")
print("The 's' character was found ",txt.count('s'), " times")
print("The 'r' character was found ",txt.count('r'), " times")
print("The 'h' character was found ",txt.count('h'), " times")
print("The 'd' character was found ",txt.count('d'), " times")
print("The 'l' character was found ",txt.count('l'), " times")
print("The 'm' character was found ",txt.count('m'), " times")
print("The 'u' character was found ",txt.count('u'), " times")
print("The 'c' character was found ",txt.count('c'), " times")


#letter_count = {}
#for letter in word:
#    if letter.isalpha():
#        letter_count[letter] += 1
#    else:
#        letter_count[letter] = 1
#print(letter_count)
            













#print(list(word).sort())
#chars = word.count("p")
#print("amount of p: ", word.lower().count("p"))
#print(words.count('p'))
# "words".lower()
#print([*words].count('p'))