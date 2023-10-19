import sys
#reading standard inputs 
test_cases = int(sys.stdin.readline())

while test_cases:
    n, m = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

# defining variables
    max_weight = 0
    running_weight = 0
    m_seen = False
    m_idx = 0

    idx = 0
#looping through Array Numbers and getting the subarray
    while idx < n:
        number = numbers[idx]
        #putting aside any number which is less than oour minimum number
        if number < m:
            running_weight = 0
            m_seen = False
            idx += 1
            continue
        #finds the minimum number
        if number == m:
            #makes sure only one minimum number is present in Subarray
            if m_seen:
                m_seen = False
                idx = m_idx + 1
                running_weight = 0
                continue
            #indicates that minimum number has been found
            else:
                m_seen = True
                m_idx = idx
        #computes the weighted sum of easch subarray and returns the maximum
        running_weight = running_weight + number
        if m_seen:
            max_weight = max(running_weight, max_weight)
        idx += 1
    test_cases -= 1
    print(max_weight)
