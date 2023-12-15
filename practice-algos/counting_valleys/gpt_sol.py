def countingValleys(steps, path):
    sea_level = 0
    valleys = 0
    in_valley = False

    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if sea_level < 0 and not in_valley:
            valleys += 1
            in_valley = True
        elif sea_level >= 0:
            in_valley = False

    return valleys

# Example usage
steps = 8
path = "DDUUUUDD"
print(countingValleys(steps, path))  # Output: 1
