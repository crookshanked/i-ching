from sys import argv

def main():
    try:
        print(argv[1])
    except IndexError:
        print("Program Missing Arg. What should I-Ching do?")
    except Exception as e:
        print("Program Failure.  Error: {}".format(e))

if __name__ == '__main__':
    main()