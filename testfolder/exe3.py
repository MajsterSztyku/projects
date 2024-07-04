# Print characters from a string that are present at an even index number

word = input("Please Enter a word: ").strip()
#word = str(word)
#print(type(word))

print("Orginal String is: ", word)
print("Printing only even index chars")

for i in range(0,len(word)):
    if i%2 == 0:
        print(i,word[i])
        