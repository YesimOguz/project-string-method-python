title = ('United statEs of america')

x = title.split()
#print(x)

lst = []
for word in x:
   capital_first_letter = word[0].upper()
   lst.append(capital_first_letter)
print("".join(lst))
print(".".join(lst))

