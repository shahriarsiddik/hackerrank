def super_reduced_string(s):
    first = 0
    second = 1
    for i in range(len(s)-1):
        if s[first] == s[second]:
            s = s[:first]+s[second+1:]
            if len(s) == 1:
                return s
            if s == '':
                return 'Empty String'
            first = 0
            second = 1
            continue
        first += 1
        second += 1
    return 'Empty String' if s=='' else s

print super_reduced_string('zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh')

# exp input
# zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
# exp output
# tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh

# s = raw_input().strip()
# result = super_reduced_string(s)
# print(result)
