import random, copy

random.seed(1234)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # number of sets

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # already same set, ie. a self-loop
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True

#PART A

def lomuto():
    pass

def quicksort():
    pass

def quickselect():
    pass


#define graph from instructions
G = {}
def mincut(G:any)->int:
    CG = copy.deepcopy(G)
    #alg goes here

    return CG

#PART B

#B1.
arr_100 = list(range(100))
arr_250 = list(range(250))
arr_500 = list(range(500))
arr_750 = list(range(750))

#Test, time, and record comparison count for:
#   Deterministic: always choose first ele of current subarray as pivot, run once for each n, record comparison count
#   Randomized: on same sorted input ^^, run 30 independent trials for each n. Report mean,max, and min comparison counts
#   Create plot with n on x axis and comparisons on y axis. Ploy deterministic count and randomized mean
#   Explain why deterministic curve is quadratic but randomized grows nlogn

#B2.
def test_karger_prob():
    res = {}
    #count min-cut results from 500 trials
    for _ in range(500):
        run = mincut(G=G)
        if run in res:
            res[run] = res[run] + 1
        else:
            res[run] = 1
    for i in sorted(res):
        print(f"Trials with min-cut = {i}: {res[i]}")
    print(f"Empirical success rate: {(res[2]/(500))*100}%")
    print(f"Theoretical success rate: {2/(8*(8-1))}% (note this is the worst case guarantee, empirical rate should be greater or equal)")
#PART C