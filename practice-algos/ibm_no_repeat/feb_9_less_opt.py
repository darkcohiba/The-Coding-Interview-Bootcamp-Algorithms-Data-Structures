def count_numbers_with_no_repeating_digits(arr):
    result = []

    for query in arr:
        n, m = query
        count = 0

        for num in range(n, m + 1):
            digits = set()
            has_repeating_digits = False

            for digit in str(num):
                if digit in digits:
                    has_repeating_digits = True
                    break
                digits.add(digit)

            if not has_repeating_digits:
                count += 1

        result.append(count)

    return result

# Example usage:
queries = [[80, 120], [100, 150], [1, 10]]
results = count_numbers_with_no_repeating_digits(queries)
print(results)
