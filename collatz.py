

def collatz(n):
    x = []
    while n != 1:
        if n % 2 == 0:
            y = (n / 2)
            x.append(y)
            n = y
        else:
            y = ((3 * n) + 1)
            x.append(y)
            n = y
    data.write(str(x) + "\n\n")


num = 1

while True:
    data = open("collatz.txt", "a")
    data.write(str(num) + "\n")
    collatz(int(num))
    num += 1
    data.close()
