"""Problem Statement:
 Given a list of integers, find the number that occurs the most times.
 If multiple elements have the same highest frequency, print the first occurring one."""

numbers=[1, 3, 2, 1, 4, 1, 3]
high=0
item=""
for num in numbers:
    count=numbers.count(num)
    if count>high:
        high=count
        item=num
        print(item)
       
    
"""Problem Statement:
 Given a list of integers, find the largest even number in the list.
 If no even number exists, print No Even Number.
"""
num=[5, 12, 3, 8, 7]
even_num=[]
for n in num:
    if n%2==0:
        even_num.append(n)
if even_num:
    print(max(even_num))
else:
    print("no even numbers")
    
    
    
"""Problem Statement:
 Given a string, check whether it is a palindrome.
 A palindrome reads the same forwards and backwards.
"""
text= "madam"   
rev=""
for t in text:
    rev=t+rev
if rev==text:
    print(" Palindrome")
else:
    print("not Palindrome")

""" Given a sentence, count the total number of words in it.
"""
sentence="Data science is interesting"
wordcount=0
for word in sentence:
    if word==" ":
        wordcount+=1
print(wordcount+1)
""" Given a list of integers, find the first duplicate element.
 If no duplicate exists, print No Duplicates.
"""
number=[3, 1, 4, 2, 3, 5]
for c in number:
    frq=number.count(c)
    if frq>1:
        print(c)
        break
else:
    print("no duplicates")
        
 
