

# # num=int(input("enter a number"))
# # fact=1
# # for i in range(1,num+1):
# #         fact=fact*i
# # print(fact)
   
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
        
#     return fact

# num=int(input("enter a number"))
# print(factorial(num))

# dict1 = {
#     "a":35,
#     "b":45
# }
# dict2={
#     "c":50,
#     "d":20
# }    
# print(dict1,dict2) 
# dict3={**dict1,**dict2}
# print(dict3)

# def palindrome(text):
#     rev=""
#     for t in text: 
#         rev=t+rev
#     if rev==text:
#         print("palindrome")
#     else:
#         print("not palindrome ")
  
# text=str(input("enter a string"))   
# print(palindrome(text))   
    
dict1={"apple":10,
       "banana":20}
dict2={"apple":30,
       "orange":40}
dict3={"apple":5,
       "banana":15}
dict4 = dict1.copy()
for key,value in dict2.items():
    if key in dict4:
        dict4[key]=dict4[key]+value
    else:
        dict4[key]=value
for key,value in dict3.items():
    if key  in dict4:
        dict4[key]=dict4[key]+value
    else:
        dict4[key]=value
print(dict4)
   