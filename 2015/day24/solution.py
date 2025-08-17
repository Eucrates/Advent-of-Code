# code run in sections due to length of time it took to generate all subsets summing to distribution weight
# these were generated in genSubset and written written to a file


import sys
from itertools import combinations

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline

tot = 0
package_weights = []
for line in lines:
    line = line.strip("\n")
    package_weights.append(int(line))
    tot += int(line)

def genSubsets(distribution_weight):
    # generate subsets that sum to distribution weight and save to a file for future use
    # subset generation code from
    # https://www.geeksforgeeks.org/python/python-program-to-get-all-subsets-having-sum-x/
    subsets = []
    def subsetSum(n, arr, x):
        for i in range(n+1):
            for subset in combinations(arr, i):
                if sum(subset) == x:
                    subsets.append(list(subset))


    subsetSum(len(package_weights), package_weights, distribution_weight)

    file = "subsets"+str(distribution_weight)
    with open(file,"w") as f:
        for subset in subsets:
            f.write(', '.join(map(str, subset)) + '\n')

def calcQE(distribution_weight):
    # calculate quantem entanglement and save to a file for future use
    file = "subsets"+str(distribution_weight)
    with open(file) as f:
        data = f.readlines()

    arrangements = []
    for line in data:
        line = line.strip("\n").split(",")
        qe  = int(line[0])
        for i, weight in enumerate(line[1:]):
            qe *= int(weight)
        arrangements.append((len(line), qe, line))

    return arrangements

def smallestQE(arrangements):

    qes = []
    smallest = 0xFFFFFFFF
    minqe = 0xFFFFFFFFFFFF
    for arrangement in arrangements:
        smallest = min(smallest, arrangement[0])

    # by inspection using the previous code, the smallest subset that sums to our distribution weight is 5 packages
    for arrangement in arrangements:
        if arrangement[0] == smallest:
            minqe = min(minqe, arrangement[1])
    return minqe

# genSubsets generates files of subsets totaling the given weight distribution
# to be used in smallestQE() function
# uncomment on first run
# genSubsets(tot//3)
# genSubsets(tot//4)

arrangements = calcQE(tot//3)
print(f"Part1: {smallestQE(arrangements)}")

arrangements = calcQE(tot//4)
print(f"Part2: {smallestQE(arrangements)}")





