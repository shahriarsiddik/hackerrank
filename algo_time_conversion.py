


import sys

def timeConversion(s):
    if s[8:] == "PM":
        if s[:2]=='12':
            return s[:-2]
        else:
            hr = int(s[:2]) + 12
            return str(hr) + s[2:-2]
    else:
        if s[:2]=='12':
            return '00'+s[2:-2]

        return s[:-2]

s = raw_input().strip()
result = timeConversion(s)
print(result)

