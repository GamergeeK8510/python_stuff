import random2


def add_employee(employee):
    data = open("people.txt", "a")
    data.write(employee + "\n")
    data.close()


def new_employee():
    with open("names.txt", 'r') as f:
        var = f.readlines()
    first = random2.randint(0, 24)
    last = random2.randint(25, 49)
    job = random2.randint(50, 54)
    time = random2.randint(0, 100)
    first_name = var[first].strip()
    last_name = var[last].strip()
    job_title = var[job].strip()
    new_emp = [first_name, last_name, job_title, str(time)]
    return "-".join(new_emp)


n = 50
while n > 0:
    string = new_employee()
    add_employee(string)
    n -= 1