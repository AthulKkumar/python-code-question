# Write an program to reverse an number
# Input: 1234
# Output: 4321

# Solution 1

def reverseNumber(number):
    reverse = 0

    while number > 0:
        # Get the last digit
        # eg 1234 % 10 = 4 , 123 % 10 = 3, 12 % 10 = 2, 1 % 10 = 1
        remainder = number % 10
        # Multiply the reverse by 10 and add the remainder
        # eg 0 * 10 + 4 = 4, 4 * 10 + 3 = 43, 43 * 10 + 2 = 432, 432 * 10 + 1 = 4321
        reverse = (reverse * 10) + remainder
        # Divide the number by 10 to get the next digit
        # eg 1234 // 10 = 123, 123 // 10 = 12, 12 // 10 = 1, 1 // 10 = 0
        number = number // 10

    return reverse

# Solution 2

def reverseNumber2(number):

    num = int(str(number)[::-1])
    return num

# Solution 3 (Using Recursion)

def reverseNumber(number):
    
        if number == 0:
            return 0
        else:
            # Get the last digit and add it to the reverse of the remaining digits
            # eg : str(1234 % 10) + str(reverseNumber(1234 // 10)) = str(4) + str(reverseNumber(123)) = str(4) + str(3) + str(reverseNumber(12)) = str(4) + str(3) + str(2) + str(reverseNumber(1)) = str(4) + str(3) + str(2) + str(1) + str(reverseNumber(0)) = str(4) + str(3) + str(2) + str(1) + str(0) = 43210
            return int(str(number % 10) + str(reverseNumber(number // 10)))
