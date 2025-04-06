import sys

def names_extractor(arg):
    with open(arg, 'r') as file:
        lines = file.readlines()
    res = "Name\tSurname\tE-mail\n"
    for line in lines:
        a = line.split(".")
        res += f"{a[0].capitalize()}\t{a[1][:-5].capitalize()}\t{line}"
    with open('employees.tsv', 'w') as file:
        file.writelines(res)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        names_extractor(arg)