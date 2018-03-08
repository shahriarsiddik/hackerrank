if __name__ == '__main__':
    N = int(raw_input())

res = []
for i in range(N):
    inp = raw_input().split()
    if inp[0] == 'print':
        print res
    else:
        if len(inp) == 1:
            eval("res.{}()".format(inp[0]))

        elif len(inp) == 2:
            eval("res.{}({})".format(inp[0], inp[1]))
        else:
            eval("res.{}({},{})".format(inp[0], inp[1], inp[2]))



        # eval("res.{}".format(inp[0])) if len(inp)==1 else eval("res.{}({},{})".format(inp[0],inp[1],inp[2])) if len(inp)==3 else eval("res.{}({})".format(inp[0],inp[1]))


    # if inp[0] == 'insert':
    #     res.insert(int(inp[1]),int(inp[2]))
    # elif inp[0] == 'print':
    #     print res
    # elif inp[0] == 'remove':
    #     res.remove(int(inp[1]))
    # elif inp[0] == 'append':
    #     res.append(int(inp[1]))
    # elif inp[0] == 'sort':
    #     res.sort()
    # elif inp[0] == 'pop':
    #     res.pop()
    # else:
    #     res.reverse()
#     print([res.insert(int(inp[1]),int(inp[2])) if inp[0] == 'insert' else res if inp[0] == 'print' else res.append(int(inp[1])) if inp[0] == 'append' else res.sort() if inp[0] == 'sort' else res.reverse()])
