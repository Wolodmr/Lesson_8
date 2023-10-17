print()

#Upper case
sentence = input('Enter the sentence  ')
print(sentence.upper())

#Count the words
print()
paragraph = input('Enter the paragraph  ')
print(f'The paragraph has {len(paragraph.split())} words')

#Digits in a string
print()
test = input('Enter the sentence. You can also enter digits there  ')
print(test.isdigit())

#Replacing characters
print()
text = input('Enter the sentence with "ao" units  ')
print(text.replace('ao', ""))

#Initials
print()
names = input('Enter your three names  ')
names_list = names.split(' ')
names_formatted = (names_list[0][0]+names_list[1][0]+names_list[2][0]).upper()
print(names_formatted)

#String length
print()
string = input('Enter any sentence  ')
print(len(string))







