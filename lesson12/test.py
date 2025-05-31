# Q3. Count Vowels in a String
# Write a function `count_vowels(text)` that returns the number of vowels (a, e, i, o, u) in a string.
# Example:
# count_vowels(&#39;hello world&#39;) -&gt; 3
# Starter Code:
def count_vowels(text):
     vowels = "aeiouAEIOU"  
    count = 0  
for char in text:
        if char in vowels:
            count += 1 

    
return count 

    
# Your code here
