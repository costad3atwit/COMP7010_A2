import random, copy, math
from collections import Counter

random.seed(1234)

#PART A

#=============    A1    ==============

def lomuto(arr:list,low:int,hi:int)->tuple[int,int]:
    pivot = arr[hi]
    i = low-1
    comparisons = 0
    for j in range(low,hi):    
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # place the pivot at the correct position
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i+1, comparisons #i+1 is where the pivot landed

# The assignment asks for the deterministic quicksort to use the first element as the pivot. 
# Lomuto uses the last element so swap it here then call the original function
def det_lomuto(arr:list,low:int,hi:int)->tuple[int,int]:
    arr[low], arr[hi] = arr[hi], arr[low]
    return lomuto(arr,low,hi)

def rand_lomuto(arr:list,low:int,hi:int)->tuple[int,int]:
    index = random.randint(low,hi)
    arr[index], arr[hi] = arr[hi], arr[index] #swap random element with last
    return lomuto(arr,low,hi)

def randQuicksort(arr:list,low:int|None = None,hi:int|None = None):
    comparisons = 0
    if low is None: #kickoff case
        low, hi = 0, len(arr)-1
    if low>= hi:
        return comparisons
    else:
        piv_ind, comps = rand_lomuto(arr,low,hi)
        left = randQuicksort(arr,low,piv_ind-1)
        right = randQuicksort(arr,piv_ind+1,hi)
        comparisons = comps + left + right
    return comparisons
        
def detQuicksort(arr:list,low:int|None = None,hi:int|None = None):
    comparisons = 0
    if low is None: #kickoff case
        low, hi = 0, len(arr)-1
    
    if low>= hi:
        return comparisons
    else:
        piv_ind, comps = det_lomuto(arr,low,hi)
        left = detQuicksort(arr,low,piv_ind-1)
        right = detQuicksort(arr,piv_ind+1,hi)
        comparisons = comps + left + right
    return comparisons

#=============    A1 END    ==============
#=============    A2    ==============

def quickselect(arr:list, k:int, low:int|None = None, hi:int|None = None):
    if low is None: #kickoff case
        low, hi = 0, len(arr)-1
    
    piv_ind, _ = rand_lomuto(arr,low,hi)
    if piv_ind == k-1:
        return arr[piv_ind]
    elif piv_ind > k-1:
        return quickselect(arr,k,low,piv_ind-1)
    else:
        return quickselect(arr,k,piv_ind+1,hi)

#=============    A2 END   ==============
#=============    A3    ==============

#define graph from instructions
G = {
    'A': Counter({'A':0, 'B':1, 'C':1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0}),
    'B': Counter({'A':1, 'B':0, 'C':1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0}),
    'C': Counter({'A':1, 'B':1, 'C':0, 'D': 1, 'E': 0, 'F': 1, 'G': 0, 'H': 0}),
    'D': Counter({'A':1, 'B':1, 'C':1, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0}),
    'E': Counter({'A':0, 'B':0, 'C':0, 'D': 1, 'E': 0, 'F': 1, 'G': 1, 'H': 1}),
    'F': Counter({'A':0, 'B':0, 'C':1, 'D': 0, 'E': 1, 'F': 0, 'G': 1, 'H': 1}),
    'G': Counter({'A':0, 'B':0, 'C':0, 'D': 0, 'E': 1, 'F': 1, 'G': 0, 'H': 1}),
    'H': Counter({'A':0, 'B':0, 'C':0, 'D': 0, 'E': 1, 'F': 1, 'G': 1, 'H': 0}),
}
def karger(G: dict) -> int:
    CG = copy.deepcopy(G)
    for vertex in CG:
        CG[vertex] = +CG[vertex] #strip zero entries

    while len(CG) > 2:
        #each undirected edge listed once with how many copies (parallel edges) it has
        edges = [
            (endpoint_a, endpoint_b)
            for endpoint_a in CG
            for endpoint_b in CG[endpoint_a]
            if endpoint_a < endpoint_b
        ]
        multiplicities = [CG[endpoint_a][endpoint_b] for endpoint_a, endpoint_b in edges]
        keep, absorbed = random.choices(edges, weights=multiplicities)[0]

        #merge the absorbed vertex into the kept vertex
        for neighbor, multiplicity in CG[absorbed].items():
            if neighbor != keep:
                CG[keep][neighbor] += multiplicity
                CG[neighbor][keep] += multiplicity
            del CG[neighbor][absorbed]   # when neighbor == keep we would create a self-loop. This removes it
        del CG[absorbed]

    # Edges remaining are the cut
    remaining_vertex = next(iter(CG))
    return sum(CG[remaining_vertex].values())

def mincut(r: int) -> int:
    return min(karger(G) for _ in range(r))

if __name__ == '__main__':
    n = len(G)
    runs = math.ceil(n * n * math.log(n)) #
    print(f"Smallest cut found in {runs} runs: {mincut(runs)}") 

#=============    A3 END    ==============


#PART B

#B1.
def test_quickselect():
    for _ in range(30):
        A = [random.randint(-50, 50) for _ in range(random.randint(1, 25))]
        k = random.randint(1, len(A))  # k is 1-based
        want = sorted(A)[k-1]
        got = quickselect(A.copy(), k)
        assert got == want

#verify expected sorting behavior
def test_quicksorts():
    for _ in range(30):
        A = [random.randint(-50, 50) for _ in range(random.randint(1, 25))]
        want = sorted(A)
        got = A.copy()
        randQuicksort(got)
        assert got == want

#not really a "test", just so counting comparisons for graphs runs with pytest
def test_time_quicksorts():
    print()
    print("Part B1 comparison counting")
    arr_100 = list(range(100))
    arr_250 = list(range(250))
    arr_500 = list(range(500))
    arr_750 = list(range(750))

    det_comps = []
    rand_comps ={100: [], 250:[], 500: [], 750:[]}
    det_comps.append(detQuicksort(arr=arr_100))
    det_comps.append(detQuicksort(arr=arr_250))
    det_comps.append(detQuicksort(arr=arr_500))
    det_comps.append(detQuicksort(arr=arr_750))
    print("Deterministic Quicksort Comparison Counts, in order of n: [100,250,500,750]")
    for i in range(4):
        print(f"Determinsitic Quicksort Comparisons {i} = {det_comps[i]}")
    for _ in range (30):
        rand_comps[100].append(randQuicksort(arr=arr_100))
        rand_comps[250].append(randQuicksort(arr=arr_250))
        rand_comps[500].append(randQuicksort(arr=arr_500))
        rand_comps[750].append(randQuicksort(arr=arr_750))
    mean_100 = sum(rand_comps[100]) / len(rand_comps[100])
    mean_250 = sum(rand_comps[250]) / len(rand_comps[250])
    mean_500 = sum(rand_comps[500]) / len(rand_comps[500])
    mean_750 = sum(rand_comps[750]) / len(rand_comps[750])
    print(f"Mean Comparison Count for Random Quicksort w/ n=100 = {mean_100}")
    print(f"Mean Comparison Count for Random Quicksort w/ n=250 = {mean_250}")
    print(f"Mean Comparison Count for Random Quicksort w/ n=500 = {mean_500}")
    print(f"Mean Comparison Count for Random Quicksort w/ n=750 = {mean_750}")
    #note: plots were created using excel and the terminal output of these print statements

#B2.

def test_karger_prob():
    print()
    print("Part B2 success rate testing")
    results = {}
    #count min-cut results from 500 trials
    for _ in range(500):
        run_res = karger(G=G)
        if run_res in results:
            results[run_res] = results[run_res] + 1
        else:
            results[run_res] = 1
    for i in sorted(results):
        print(f"Trials with min-cut = {i}: {results[i]}")
    print(f"Empirical success rate: {(results[2]/(500))*100}%")
    print(f"Theoretical success rate: {2/(8*(8-1))}% (=2/[n(n-1)])\n    (note this is the worst case guarantee, empirical rate should be greater or equal)")
