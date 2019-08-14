import random

f = open('quotes.txt', 'r')
lines = f.readlines()

def get_random_quote():
    """
    Returns a random quote from quotes.txt
    """
    return random.choice(lines)

if __name__ == '__main__':
    main()