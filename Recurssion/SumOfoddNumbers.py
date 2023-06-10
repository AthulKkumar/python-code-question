# The program to print the sum of odd numbers whithin an range


def sumOfOdd(num1, num2):

    if num1 > num2  :
        return 0
    
    return num1 + sumOfOdd(num1 + 2, num2)

num1 = 1
num2 = int(input())
print(sumOfOdd(num1, num2))