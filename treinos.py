def is_leap(year):
    leap = False
    
    if year % 4 == 0 or year % 400 == 0:
        return True
    elif year % 100 == 0:
        return leap
    else:
        return leap

#year = int(input())
#print(is_leap(year))


year = 1900
print(is_leap(year))


year = 2100
print(is_leap(year))

