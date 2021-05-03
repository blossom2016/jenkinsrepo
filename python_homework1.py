# Create a function that takes a string and returns the number (count) of vowels contained within it.
#
# Examples
# count_vowels("Celebration") ➞ 5
# count_vowels("Palm") ➞ 1
# count_vowels("Prediction") ➞ 4
#
# Notes
# a, e, i, o, u are considered vowels (not y).
# All test cases are one word and only contain letters.

def count_vowels(word: str) -> int:
     # Your Code comes here.
    count =0
    vowel='aeiou'
    for i in word:
        if i in vowel:
            count=count+1        
    return count
 
print(count_vowels("Celebration")) 
print(count_vowels("Palm")) 
print(count_vowels("Prediction"))
#message=input("Enter a word to see how many vowels are in it ")
#print(count_vowels(message.lower())," Vowels are in ", message)
  # instatce count==0
  # i get a string from user, then compare each letter in the string to see if it matches any item in the vowel
  
  # if it matches, add to count 
  # print new count 
 