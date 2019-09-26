import random
import os

file_path = os.path.dirname(os.path.realpath(__file__)) + "/quotes.txt"
f = open(file_path, "r")
lines = f.readlines()


def get_random_quote():
    """
    Returns a random quote from quotes.txt
    """
    return random.choice(lines)


if __name__ == "__main__":
    main()
