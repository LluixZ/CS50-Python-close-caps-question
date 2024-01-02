import sys
import csv

codelines = []

def main():
    check_lines()
    lines = check_valid()
    print(lines)


def check_lines():
    if len(sys.argv) <2:
        print('To few arguments')
        sys.exit()
    elif len(sys.argv) >2:
        print('To many arguments')
        sys.exit()
    else:
        if not '.py' in sys.argv[1]:
            print('Not a python file')
            sys.exit()
        else:
            pass


def check_valid():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            countline = 0
            for row in reader:
                if not row:
                    continue
                textline = row[0]
                codelines.append(textline)
                if textline.startswith('#') or textline.rstrip() == '':
                    countline +=0
                else:
                    countline +=1
            return countline
    except FileNotFoundError:
        print('File does not exist')
        sys.exit()


if __name__ == '__main__':
    main()
