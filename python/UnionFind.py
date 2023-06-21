# from neetcode soln 684 https://www.youtube.com/watch?v=FXWRE67PLL0

# graph, list of edges, n edges, n vertices. vertices indexed from 1 
# two arrays, one for value/numbering and another for rank
# 
# par array [0,1,2,3,] i.e index = value
# rank array [1,1,1,1,1,] 
par = [i for i in range(len(edges)+1)]
rank = [1] * (len(edges)+1)

def find(n):
  p = par[n]
  while p != par[p]:        #   [0,1,2,1,4,3]  [5] = 3, [3] = 1, [1] = 1
    par[p] = par[par[p]]    #   path compression [5] = [3] = 1
    p = par[p]
   return p

def union(n1,n2):            #    [
  p1, p2 = find(n1), find(n2)
  if p1 == p2:        
    return False              # already in union set
  if rank[p1] > rank[p2]:
    par[p2] = p1
    rank[p2] += rank[p1]
   else:  
    par[p1] = p2
    rank[p1] += rank[p2]
   return True
