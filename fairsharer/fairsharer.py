def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.

    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args
        values:
            1D array of values (list or numpy array)
        num_iteration:
            Integer to set the number of iterations
        share:
            Fraction given to each neighbor
    """
    
    values = list(values)

    for _ in range(num_iterations):
        values_new = values.copy()

        # Find the highest value and its index
        max_value = max(values)
        max_index = values.index(max_value)

        # Amount that will be shared
        amount = share * max_value

        # Find left and right neighbors
        left_index = (max_index - 1) % len(values)
        right_index = (max_index + 1) % len(values)

        # Update the values
        values_new[max_index] -= 2 * amount
        values_new[left_index] += amount
        values_new[right_index] += amount

        # Use the new values for the next iteration
        values = values_new

    return values_new