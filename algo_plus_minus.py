arr = [-4, 3, -9, 0, 4, 1]

pos_count = 0
neg_count = 0
zero_count = 0

for i in arr:
    if i<0:
        neg_count+=1
    elif i > 0:
        pos_count += 1
    else:
        zero_count+=1

print abs(pos_count*1.0/len(arr))
print abs(neg_count*1.0/len(arr))
print abs(zero_count*1.0/len(arr))
