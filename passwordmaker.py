import random2


def password():
    i = 15
    p = []
    while i > 0:
        with open("password.txt", 'r') as f:
            chars = f.readlines()
        index = random2.randint(0, len(chars) - 1)
        char = chars[index].strip()
        p.append(char)
        i -= 1
    print("".join(p))


while True:
    stop = input("")
    password()
    if stop == "stop":
        break
