def super_reduced_string(s):
    temp = None
    res = ''
    count = 0
    lnth = len(list(s))
    for i in s:
        count += 1
        if temp is None:
            if count == lnth:
                res += i
            temp = i
        elif i == temp:
            temp = None
        else:
            res += temp
            temp = i
            if count == lnth:
                res += i
    super_reduced_string(res)
    return 'Empty String' if res == '' else res


# print super_reduced_string('baab')

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
