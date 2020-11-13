import random2


class Employee:

    total_employees = 0
    employees = []

    def __init__(self, first, last, job, time):
        self.first = first
        self.last = last
        self.t = int(time)
        self.email = first + "." + last + "@pythoncomp.org"

        if job == "jan":
            job_base = 40000
            self.job = "Janitor"

        elif job == "rec":
            job_base = 55000
            self.job = "Receptionist"

        elif job == "mar":
            job_base = 65000
            self.job = "Marketing"

        elif job == "man":
            job_base = 75000
            self.job = "Manager"

        elif job == "dev":
            job_base = 90000
            self.job = "Developer"

        else:
            job_base = 60000
            self.job = "Assistant"

        if int(time) <= 12:
            self.salary = job_base * 0.98976432

        elif int(time) <= 52:
            self.salary = ((job_base * (1 + (0.2 / int(time)) ** int(time)) / 2) + job_base / 2) * 0.98976432

        elif int(time) <= 78:
            self.salary = job_base * (1 + (0.2 / int(time)) ** int(time)) * 1.00851356845

        elif int(time) > 78:
            self.salary = job_base * (1 + (0.25 / int(time)) ** int(time)) * 1.0158794513

        Employee.total_employees += 1
        Employee.employees.append([str(Employee.total_employees),
                                   str(self.full_name()),
                                   str(self.job),
                                   str(self.email),
                                   str(self.salary),
                                   str(self.t)])

    def full_name(self):
        first = self.first
        last = self.last
        return "{} {}".format(first.replace(first[0], first[0].upper(), 1), last.replace(last[0], last[0].upper(), 1))

    @classmethod
    def from_doc(cls, string):
        first, last, job, time = string.split("-")
        cls(first, last, job, time)

    @classmethod
    def list_employees(cls):
        x = 0
        while x != cls.total_employees:
            print("\n".join(cls.employees[x]))
            print("")
            x += 1

    @classmethod
    def add_employees(cls, file_name):
        with open(file_name, 'r') as f:
            doc = f.readlines()
            x = len(doc) - 1
            while x > - 1:
                transfer = doc[x].strip()
                cls.from_doc(transfer)
                x -= 1

    @classmethod
    def export_employees(cls):
        x = 0
        while x != cls.total_employees:
            data = open("employees.txt", "a")
            data.write("\n".join(cls.employees[x]))
            data.write("\n \n")
            data.close()
            x += 1


Employee.add_employees("people.txt")
Employee.list_employees()
Employee.export_employees()
