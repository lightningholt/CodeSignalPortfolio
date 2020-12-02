def depositProfit(deposit, rate, threshold):
    '''
    You have deposited a specific amount of money into your bank account.
    Each year your balance increases at the same rate.
    With the assumption that you don't make any additional deposits,
    find out how long (how many years) it would take for your balance to pass a specific threshold.
    '''

    year = 0
    while deposit < threshold:
        year += 1
        deposit *= 1+(0.01*rate)


    return year
