n = 5
# **********Right angle triangle*********

# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")

#     print()    

# ************Left angle triangle**********

# for i in range(n):

#     for j in range(n-i):
#         print(" ",end=" ")

#     for j in range(i):
#         print('*',end=" ")    

#     print()

#  **********Hill**********

for i in range(n):
    
    for j in range(n-i):
        print(" ",end=" ")

    for j in range(i-1): 
        print('*',end=" ") 

    for j in range(i): 
        print('*',end=" ")              
    
    print()


###################################### NUMBER PATTERNS ##########################################

# for i in range(n):
#     v = 1
#     for j in range(n-i):
#         print(" ",end=' ')

#     for j in range(i):
#         print(v,end=" ") 
#         v += 1 

#     for j in range(i-1):
#         print(v,end=" ") 
#         v -= 1       

#     print()    