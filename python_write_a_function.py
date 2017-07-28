def is_leap(year):
    leap = False
    # Write your logic here
    if not year%400:
        leap = True
    elif not year%100 and not year%4:
        leap= leap
    elif not year%4:
        leap = True
    return leap

print is_leap(2400)