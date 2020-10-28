def seatsInTheater(nCols, nRows, col, row):
    # want to return the number of seats behind your seat and to the left.
    # so for a 5x5 theater and sitting in the middle seat
    # the theater would look like
    # [ 0 0 1 1 1]
    # [ 0 0 1 1 1]
    # [ 0 0 1 1 1]
    # [ 0 0 0 0 0]
    # [ 0 0 0 0 0]
    # (with 1's representing people behind and to the left)
    return (nCols - col + 1) * (nRows - row)
