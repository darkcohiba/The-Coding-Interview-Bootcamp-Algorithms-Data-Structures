def sockMerchant(n, ar):
    color_counts = {}
    for color in ar:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    return sum(count // 2 for count in color_counts.values())

# Example usage
n = 7
ar = [1, 2, 1, 2, 3, 1, 2]
print(sockMerchant(n, ar))  # Output: 2
