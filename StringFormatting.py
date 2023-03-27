# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each  from  to . 
# Each value should be space-padded to match the width of the binary value of .


def print_formatted(number):
    length = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(length),str(oct(i)[2:]).rjust(length),str(hex(i)[2:]).upper().rjust(length),str(bin(i)[2:]).rjust(length))

# Input Format
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)