
#counting number of vowels in a  sentence
# vowels={"a":0,"i":0,"e":0,"o":0,"u":0}

# str=input("Please enter a sentence : ")
# for i in str:
#     if i in vowels:
#         vowels[i]=vowels[i]+1
# print(vowels)
# Count the occurrence of each alphabhet in the string entered by the user

letters={"a":0,"b":0,"c":0,"d":0,"e":0}

str=input("Please enter a sentence :")
for i in str:
    if i in letters:
        letters[i]=letters[i]+1
print(letters)