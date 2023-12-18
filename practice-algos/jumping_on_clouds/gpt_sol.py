def min_jumps(clouds):
    """
    This function finds the minimum number of jumps required to traverse
    the cloud array while avoiding thunderheads (represented by 1).
    
    :param clouds: list of integers (0 for safe, 1 for thunderhead)
    :return: minimum number of jumps
    """
    n = len(clouds)
    jumps = 0
    i = 0

    while i < n - 1:
        # If possible, make a jump of 2, else jump by 1
        if i + 2 < n and clouds[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1

    return jumps

# Example usage
clouds_example = [0, 1, 0, 0, 0, 1, 0]
min_jumps(clouds_example)
