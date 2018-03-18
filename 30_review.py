def even_odd(inp):
    even = ""
    odd = ""

    for i in range(len(inp)):
        if i%2 == 0:
            even+=inp[i]
        else:
            odd += inp[i]
    return " ".join([even,odd])

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        inp = input().strip()
        print(even_odd(inp))
