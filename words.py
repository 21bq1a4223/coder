names=['arun','varun','kent','eat','pot','net','peak','peacock','zebra','nato','toe','poke',knife','peot','venus','ant']
letters=['A','K','E','O','T','P','N']
for name in names:
    c=0
    l=list(set(name.upper()))
    for letter in l:
        if letter in letter:
            c+=1
        if c==len(name):
            print(names)