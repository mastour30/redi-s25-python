# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
my_list=["redi","scholl","2032","spring"]
count=0
for word in my_list:
   
    if word[0]==word[-1] and len(word)>=2:
        print(word)
        count+=1
        
print(count)
