def centuryFromYear(year):
    cent = year//100
    rem = year % 100
    if rem == 0:
        return cent
    else:
        return cent + 1
