letter_count={}
data="This is string with upper case letter"
data=data.lower()
for letter in data:
    letter_count[letter]=letter_count.get(letter, 0)+1
    
    letter_items=list(letter_count.items())
    letter_items.sort()
print (letter_items)

