# To fin the total number of occurance of a string in a given string
# string = 'ABCDAB'
# print(string[6:100])
def count_substring(string, sub_string):
    ml = len(string)
    sl = len(sub_string)
    c =0 
    for i in range(0,ml):
        # print(string[i:(sl+i)]) takes no of characters from the string as the length of the sub string
        if(string[i:(sl+i)]==sub_string):
            c = c+1
        
    return c
# Input
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)