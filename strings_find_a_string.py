def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        print(i)
        if 'CDC' == string[i:i+len(sub_string)]:
            count += 1
    return count

print(count_substring("ABCDCDC","CDC"))