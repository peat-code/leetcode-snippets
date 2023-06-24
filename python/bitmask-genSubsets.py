arr = ['a','b','c']
ans = []
for i in range(1<<3):
    currentSet=[]
    for j in range(3):
        if(i & 1<<j):
            currentSet.append(arr[j])
    ans.append(currentSet)    
print(ans)

"""
Output
[[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
"""
