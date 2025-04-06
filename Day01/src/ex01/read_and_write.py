def read_and_write():
    with open('ds.csv', 'r') as file:
        lines = file.readlines()
    res = ""
    for line in lines:
        quote = False
        for i in line:
            if i == '"':
                quote = not(quote)
            if quote == False and i == ',':
                res += '\t'
            else:
                res += i
    with open('ds.tsv', 'w') as file:
        file.writelines(res)

if __name__ == '__main__':
    read_and_write()