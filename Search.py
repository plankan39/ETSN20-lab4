import os


def search(args):
    if args[0] != "search":
        return ["wrong format"]

    searchFile = args[-1]
    if not os.path.isfile(searchFile):
        return ["could not find file: " + searchFile]

    pattern = " ".join(args[1:-1])
    print(repr(pattern) + " appears in the following lines: \n")

    f = open(searchFile, "r")

    result = []
    for l in f.readlines():
        if pattern in l:
            result.append(l)

    f.close()
    return result

def main():
    args = [""]
    while args[0] != "q":
        args = input("enter command('q' to quit): ").split(" ")
        res = search(args)
        for line in res:    
            print(line)

if __name__ == '__main__':
    main()
