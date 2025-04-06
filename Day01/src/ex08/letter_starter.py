import sys

def letter_starter(arg):
    with open("employees.tsv", 'r') as file:
        lines = file.readlines()
    for line in lines:
        sp = line.split('\t')
        if sp[2] == arg + "\n":
            print(f"Dear {sp[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
    
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        letter_starter(arg)