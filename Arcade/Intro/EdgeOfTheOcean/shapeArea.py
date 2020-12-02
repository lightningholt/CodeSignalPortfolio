def shapeArea(n):
    # find area of iteratively created shape.
    # Iterative process:
    # After initial seed created,
    # shape expands into surrounding regioin
    
    area = 0
    for i in range(n):
        if i == 0:
            area += 1
        else:
            area += 4 * (i)

    return area
