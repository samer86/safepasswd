import string
import random
'''
Random Password Generator using Python
'''

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
symbols_modified = '$@-_!'
# string.ascii_letters

# combine the data
all = lower + upper + symbols_modified + num + lower+num + symbols_modified

# all = lower + upper + num + symbols_modified


def GeneratePass(length): return "".join(random.sample(all, length))


def main():
    print(GeneratePass(20))


if __name__ == '__main__':
    main()
