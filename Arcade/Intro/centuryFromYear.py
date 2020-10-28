def centuryFromYear(year):
    # Find the century from a given year
    cent = year//100
    rem = year % 100
    if rem == 0:
        return cent
    else:
        return cent + 1 # cause we count centuries from 0 (year 0 is in the first century)
