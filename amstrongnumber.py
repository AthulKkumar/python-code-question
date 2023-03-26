# n = input("Enter the number")
# a=[]
# for i in n:
#     # print(i)
#     num = int(i)
#     sq = num**len(n)
#     a.append(sq)
    
# print(sum(a))
# n = "aathul"
# def  recurive(n):
#     print(n)
#     if (n == 0):
#         print('enter an numer')
#     else:
#         for i in n:
#             pass    

# def removeDuplicates(myString): 
  
#     # If length is 1 or 0 
#     if len(myString) == 0 or len(myString) == 1: 
#         return myString 
  
#     # Check for adjacent characters 
#     if myString[0] == myString[1]: 
#         # If found, remove them
#         # print(myString[1:])
#         new_myString = myString[1:] 
#         return removeDuplicates(new_myString) 
  
#     # If not found, keep character and move ahead 
#     return myString[0] + removeDuplicates(myString[1:]) 
  
# # Driver Code 
# str1 = "geeksforgeeg"
# print(removeDuplicates(str1))
