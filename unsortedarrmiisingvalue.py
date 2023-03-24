arr = [1,3,2,5,5]

def Ans(arr):

    ans = [0]*len(arr)
    # print(ans)
    for i in arr:
        ans[i-1] = 1
    print(ans)    

    for i in range(len(arr)):
        # print(i)
        if ans[i] == 0:
            return i+1
    # return -1    

elem = Ans(arr)
print(elem)
