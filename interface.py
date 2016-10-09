# Type this in your console: python interface.py asdf
# > asdf
# Now type: python interface.py run bagua
# > What will it say??

from sys import argv

def main():
    try:
        if(argv[1] == "run" and argv[2] == "bagua"):
          print("Excellent! Now let's get to work!")
        else:
          print(argv[1])
    except IndexError:
        print("Program Missing Arg. What should I-Ching do?")
    except Exception as e:
        print("Program Failure.  Error: {}".format(e))

if __name__ == '__main__':
    main()
