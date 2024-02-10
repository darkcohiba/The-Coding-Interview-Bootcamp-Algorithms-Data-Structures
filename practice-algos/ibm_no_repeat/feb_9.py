def print_numbers_with_no_repeating_digits(arr):
    def has_repeating_digits(num_str):
        return len(set(num_str)) != len(num_str)

    for query in arr:
        n, m = query[0], query[1]
        count = 0

        for num in range(n, m + 1):
            if not has_repeating_digits(str(num)):
                count += 1

        print(count)

# Example usage:
queries = [[1, 20], [9, 19]]
print_numbers_with_no_repeating_digits(queries)