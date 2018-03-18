res_dict = {}


def make_res_dict(inp):
    inp = inp.split()
    res_dict[inp[0]] = inp[1]


def check_res_dict(name):
    if name in res_dict.keys():
        print("=".join([name , res_dict[name]]))
    else:
        print("Not found")


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        make_res_dict(input().strip())

    for _ in range(n):
        check_res_dict(input().strip())



