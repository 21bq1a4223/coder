names=['Arun','Varun','kent','eat','pot','net','peak','peacock','zebra','nato','toe','poke','knife','peot','venus','ant']
letters=['A','K','E','O','T','P','N']
for name in names:
    cnt=0
    uni=list(set(name.upper()))
    for letter in uni:
        if letter in letters:
            cnt+=1
    if cnt==len(name):
        print(name)
    