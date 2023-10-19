import sys
# reading standard inputs
test_cases = int(sys.stdin.readline())

while test_cases:
    r, c = map(int, sys.stdin.readline().split())

#getting number of arrangments ensuring its <= MOD
    MOD = 10**9+7
    print(pow(3, r+c, MOD)*pow(2, r*c, MOD)%MOD)
    test_cases -= 1
