#Title of the program written by Siergiey Kolisnichenko
print("Pig Latin Translator")
#Vowel definition 
vowels=['a','e','o','u','y','i','A','E','O','U','Y','I']
#Entered a space for an aesthetic purpose
print("")
#An input field
x=input("Please enter your phrase:")
#A prompt that pops up when there was no text entered
if x=="":
   print("You didn't enter anything")
   x=input("Please enter your phrase... Again:")
#Length counter
print(len(x))
#In this part sentences are being split into words
words=x.split(" ")
#A container for translated words
translatedWords=[]
print(words)
#Defined variables in words as "v"
for v in words:
#Here all the magic happens, regular words are being translated to Pig Latin
#Added a failsafe if somebody would enter an empty space in a sentence 
        if v=="":
            continue
#words starting with a vowel
        elif v[0] in vowels:
            translatedWords.append(v[0:]+"way")
#Words starting with one consonant
        elif v[0] not in vowels and v[1] in vowels:
            translatedWords.append(v[1:]+v[0]+"ay")
#Words starting with two consonants
        elif v[0] and v[1] not in vowels:
            translatedWords.append(v[2:]+v[0]+v[1]+"ay")
#Translated words are being put together in a sentence
print("Your translation is:", *translatedWords)
