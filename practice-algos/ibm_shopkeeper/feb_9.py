def min_moves_to_median(price, k):
    n = len(price)
    
    # Step 1: Sort the array
    price.sort()

    # Step 2: Find the current median
    current_median = price[n // 2]

    # Step 3: Calculate the difference between current median and desired median
    moves = abs(current_median - k)

    # Step 4: Iterate through prices and calculate total moves
    for i in range(n // 2):
        if price[i] > k:
            moves += price[i] - k

    for i in range(n // 2 + 1, n):
        if price[i] < k:
            moves += k - price[i]

    # Step 5: Return the total number of moves
    return moves

# Example usage:
n = int(input())
price = [int(input()) for _ in range(n)]
k = int(input())
result = min_moves_to_median(price, k)
print("Minimum moves:", result)