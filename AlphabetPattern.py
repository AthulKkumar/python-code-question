# Printing the alphabet inn pattern
n = int(input("Enter the number"))
# ''' ord() function returns the unicode code point for the specified character'''
k = ord('A') 

for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(k+j),end=" ")
    print()   

    # output 
    # A 
    # A B
    # A B C
    # A B C D

for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k = k+1
    print()


    # output 
    # A
    # B C
    # D E F
    # G H I J