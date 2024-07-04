# Return the count of a given substring from a string

input_txt = input("Paste your text here:  ").lower()
search_txt = input("Enter the word that you want to search in the given text: ").lower()
x = input_txt.count(search_txt)
                    
print(search_txt ,'appeared ', x, "times.")