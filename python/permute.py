# n! permutations. O(n . n!)
def toStr(ListA):
    return "".join(ListA)

def permute(ListB,start,end):
    if start==end:
        print(toStr(ListB))
        print('\n')
    for i in range(start,end):
        # swap i th with start
        ListB[i],ListB[start] = ListB[start],ListB[i]
        print("Swaps at ", ListB[i],ListB[start])
        permute(ListB,start+1,end)
        ListB[i],ListB[start] = ListB[start],ListB[i]
        print("Swaps at ", ListB[i],ListB[start])


string="boat"
n = len(string)
arr = list(string)
permute(arr,0,n)
