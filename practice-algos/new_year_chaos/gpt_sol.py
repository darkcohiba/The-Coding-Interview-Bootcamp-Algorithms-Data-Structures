def minimumBribes(q):
    bribes = 0
    n = len(q)
    for i in range(n - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count the number of bribes
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

# Example usage
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])  # Normal case
minimumBribes([4, 1, 2, 3])              # Too chaotic case
