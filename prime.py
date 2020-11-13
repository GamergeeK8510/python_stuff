
def prime(n, p):
    i = 2
    u = [2, 3, 5, 7]
    if n >= 10:
        while i <= (int(n) / 2) and p == 0:
            mod = int(n) % i
            if mod == 0:
                print("Not Prime")
                p += 1
            else:
                i += 1
        if p == 0:
            print("Prime")
        else:
            pass
    elif n in u:
        print("Prime")
    else:
        print("Not Prime")


while True:
    num = input("[]: ")
    if num == "stop":
        break
    else:
        prime(int(num), 0)









