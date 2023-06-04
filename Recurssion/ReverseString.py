# Write an program toprint the reverse of a string. Using Recursion

# Solution 1:
def reverseString(s, indx):
    if indx == len(s):
        return ""
    
    temp = s[indx]
    reverseString(s, indx+1)
    print(temp, end="")


# Solution 2:

def reverseString(string):
    # Base Case
    if len(string) == 0:
        return string
    else:
        # Recursive Case
        # First it will call the function with string[1:] and then it will add the first character of the string
        return reverseString(string[1:]) + string[0]
    
string = input("Enter a string: ")
print("Reverse of string is: ", reverseString(string))

# Otuput :
# Enter a string: Hello
# Reverse of string is:  olleH