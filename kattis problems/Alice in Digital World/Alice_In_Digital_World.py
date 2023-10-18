import sys

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
#looping through Array Numbers and getting the submay
    while idx < n:
        number = numbers[idx]

        if number < m:
            running_weight = 0
            m_seen = False
            idx += 1
            continue

        if number == m:
            if m_seen:
                m_seen = False
                idx = m_idx + 1
                running_weight = 0
                continue
            else:
                m_seen = True
                m_idx = idx

        running_weight = running_weight + number
        if m_seen:
            max_weight = max(running_weight, max_weight)
        idx += 1
    test_cases -= 1
    print(max_weight)