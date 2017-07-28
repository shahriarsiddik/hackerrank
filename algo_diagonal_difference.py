inp = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diag_l_r = 0
diag_r_l = 0
for i in range(len(inp)):
    diag_l_r += inp[i][i]
    diag_r_l += inp[i][-(i+1)]
print abs(diag_l_r-diag_r_l)