
# f(i) is defined as the number of ways to attend the first i days having attended the i-th day
# f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)
# f(4) = f(3) + f(2) + f(1) + f(0) => 8
# f(1) = 1, f(2) = 2, f(3) = 4(AAP, APP, PAP, PPP)
# f(4) = 8 (PPPP, AAAP, AAPP, APAP, PPAP, APPP, PAAP, PAPP)
# n <=3 -> case needs to be handled so we can initialize f(0) = 1
n = int(input())
ways = [0 for i in range(n+1)]
ways[0] = 1

def compute_ways(n):
    global ways
    if n < 0:
        return 0
    elif ways[n] !=0:
        return ways[n]
    else:
        ways[n] = compute_ways(n-1) + compute_ways(n-2) + compute_ways(n-3) + compute_ways(n-4)
    return ways[n]

# 1. The number of ways to attend classes over N days.
# f(n) + f(n-1) + f(n-2) + f(n-3)
# 
compute_ways(n)
# print("WAYS ", ways)
print("Q1. The number of ways to attend classes over N days and graduate is - ")
tot_ways = 0
if n >= 3:
    tot_ways = ways[n] + ways[n-1] + ways[n-2] + ways[n-3]
else:
    tot_ways += ways[n]
    if n -1 >=0:
        tot_ways += ways[n-1]
    if n-2 >=0:
        tot_ways += ways[n-2]
    if n-3 >=0:
        tot_ways += ways[n-3]

print(tot_ways)

print("Q2. The probability that you will miss your graduation ceremony.")
print(1 - tot_ways/(2 ** n))
    
    
