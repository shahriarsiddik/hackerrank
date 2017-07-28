# 07:05:45PM
time = "07:05:45PM"

if time[8:]=="PM":
    hr = int(time[:2])+12
    print str(hr)+time[2:-2]
else:
    print time[:-2]

