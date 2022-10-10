def containsVowels(string):
    string=string.lower()
    for char in string:
        if char in "aeiouAEIOU":
            return True
    return False
print(containsVowels("EDUCATION"))
print(containsVowels("AUTOMOBILE"))        
print(containsVowels("EVACUATION"))
print(containsVowels("REMUNERATION"))
print(containsVowels("REGULATION"))
print(containsVowels("VARSHINI"))