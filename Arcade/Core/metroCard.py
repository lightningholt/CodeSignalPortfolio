def metroCard(lastNumberOfDays):
    if lastNumberOfDays < 31:
        return [31]
    else:
        return [28, 30, 31]
